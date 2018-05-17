# stdlib imports
import os
import pickle
from math import pi, sqrt


# local imports
from . import log
from .sample import MC, Signal


class Higgs(MC, Signal):
    MASSES = range(100, 155, 5)

    NORM_BY_THEORY = True

    def __init__(self, year,
                 mode='gg', modes=None,
                 mass=None, masses=None,
                 channel=None,
                 sample_pattern=None, # i.e. PowhegJimmy_AUET2CT10_ggH{0:d}_tautauInclusive
                 ggf_weight=False,
                 vbf_weight=False,
                 suffix=None,
                 label=None,
                 inclusive_decays=False,
                 **kwargs):
        self.channel=channel
        self.inclusive_decays = inclusive_decays
        if masses is None:
            if mass is not None:
                assert mass in Higgs.MASSES
                masses = [mass]
            else:
                # default to 125
                masses = [125]
        else:
            assert len(masses) > 0
            for mass in masses:
                assert mass in Higgs.MASSES
            assert len(set(masses)) == len(masses)

        if modes is None:
            if mode is not None:
                assert mode in Higgs.MODES
                modes = [mode]
            else:
                # default to all modes
                modes = Higgs.MODES
        else:
            assert len(modes) > 0
            for mode in modes:
                assert mode in Higgs.MODES
            assert len(set(modes)) == len(modes)

        name = 'Signal'

        str_mode = ''
        if len(modes) == 1:
            str_mode = modes[0]
            name += '_%s' % str_mode
        elif len(modes) == 2 and set(modes) == set(['W', 'Z']):
            str_mode = 'V'
            name += '_%s' % str_mode

        str_mass = ''
        if len(masses) == 1:
            str_mass = '%d' % masses[0]
            name += '_%s' % str_mass

        if label is None:
            label = '%s#font[52]{H}(%s)#rightarrow#tau#tau' % (
                str_mode, str_mass)

        if year == 2011:
            if suffix is None:
                suffix = '.mc11c'
            generator_index = 1
        elif year == 2012:
            if suffix is None:
                suffix = '.mc12a'
            generator_index = 2
        #Fix Me later
        elif (year == 2015 or year == 2016):
            if suffix is None:
                suffix= ''
            generator_index = 3
        else:
            raise ValueError('No Higgs defined for year %d' % year)

        self.samples = []
        self.masses = []
        self.modes = []

        if sample_pattern is not None:
            assert len(modes) == 1
            for mass in masses:
                self.masses.append(mass)
                self.modes.append(modes[0])
                self.samples.append(sample_pattern.format(mass) + '.' + suffix)
        else:
            for mode in modes:
                generator = Higgs.MODES_DICT[mode][generator_index]
                for mass in masses:
                    if self.channel=='lephad':
                        pattern='%s%sH%d_ttlh%s' % (
                            generator, mode, mass, suffix)
                    else:
                        pattern='%s%sH%d_tautauhh%s' % (
                            generator, mode, mass, suffix)
                    
                    self.samples.append(pattern)    
                    self.masses.append(mass)
                    self.modes.append(mode)

        if len(self.modes) == 1:
            self.mode = self.modes[0]
        else:
            self.mode = None
        if len(self.masses) == 1:
            self.mass = self.masses[0]
        else:
            self.mass = None

        self.ggf_weight = False#ggf_weight
        self.ggf_weight_field = 'ggf_weight'
        self.vbf_weight = False#vbf_weight
        self.vbf_weight_field = 'vbf_weight'
        # use separate signal files by default
#        kwargs.setdefault('student', 'hhskim_signal')
        super(Higgs, self).__init__(
            year=year, label=label, name=name, **kwargs)

    #def weight_systematics(self):
    #    systematics = super(Higgs, self).weight_systematics()
    #    if self.ggf_weight:
    #        systematics.update({
    #            'QCDscale_ggH1in'})
    #    return systematics

    def weight_fields(self):
        fields = super(Higgs, self).weight_fields()
        if self.ggf_weight:
            fields.append(self.ggf_weight_field)
        if self.vbf_weight:
            fields.append(self.vbf_weight_field)
        return fields

    def histfactory(self, sample, category, systematics=False,
                    rec=None, weights=None, mva=False,
                    uniform=False, nominal=None):
        if not systematics:
            return
        if len(self.modes) != 1:
            raise TypeError(
                'histfactory sample only valid for single production mode')
        if len(self.masses) != 1:
            raise TypeError(
                'histfactory sample only valid for single mass point')

        # isolation systematic
        sample.AddOverallSys(
            'ATLAS_ANA_HH_{0:d}_Isolation'.format(self.year),
            1. - 0.06,
            1. + 0.06)

        mode = self.modes[0]

        if mode in ('Z', 'W'):
            _uncert_mode = 'VH'
        else:
            _uncert_mode = self.MODES_WORKSPACE[mode]

        if self.year == 2011:
            energy = 7
        elif self.year == 2012:
            energy = 8
        else:
            raise ValueError(
                "collision energy is unknown for year {0:d}".format(self.year))

        # QCD_SCALE
        for qcd_scale_term, qcd_scale_mode, qcd_scale_category, values in self.QCD_SCALE:
            if qcd_scale_mode == _uncert_mode and qcd_scale_category == category.name:
                high, low = map(float, values.split('/'))
                sample.AddOverallSys(qcd_scale_term, low, high)

        # UE UNCERTAINTY
        for ue_term, ue_mode, ue_category, values in self.UE_UNCERT:
            if ue_mode == _uncert_mode and ue_category == category.name:
                high, low = map(float, values.split('/'))
                sample.AddOverallSys(ue_term, low, high)

        # PDF ACCEPTANCE UNCERTAINTY (OverallSys)
        for pdf_term, pdf_mode, pdf_category, values in self.PDF_ACCEPT_NORM_UNCERT:
            if pdf_mode == _uncert_mode and pdf_category == category.name:
                high, low = map(float, values.split('/'))
                sample.AddOverallSys(pdf_term, low, high)

        sample_nom = sample.hist

        # PDF ACCEPTANCE UNCERTAINTY (HistoSys) ONLY FOR MVA
        if mva:
            for pdf_term, pdf_mode, pdf_category, hist_names in self.PDF_ACCEPT_SHAPE_UNCERT:
                if pdf_mode == _uncert_mode and pdf_category == category.name:
                    high_name, low_name = hist_names.format(energy).split('/')
                    high_shape, low_shape = self.PDF_ACCEPT_file[high_name], self.PDF_ACCEPT_file[low_name]
                    if len(high_shape) != len(sample.hist):
                        log.warning("skipping pdf acceptance shape systematic "
                                    "since histograms are not compatible")
                        continue
                    high = sample_nom.Clone(shallow=True, name=sample_nom.name + '_{0}_UP'.format(pdf_term))
                    low = sample_nom.Clone(shallow=True, name=sample_nom.name + '_{0}_DOWN'.format(pdf_term))
                    high *= high_shape
                    low *= low_shape
                    histsys = histfactory.HistoSys(
                        pdf_term, low=low, high=high)
                    sample.AddHistoSys(histsys)

        # BR_tautau
        _, (br_up, br_down) = yellowhiggs.br(
            self.mass, 'tautau', error_type='factor')
        sample.AddOverallSys('ATLAS_BR_tautau', br_down, br_up)

        # <NormFactor Name="mu_BR_tautau" Val="1" Low="0" High="200" />
        sample.AddNormFactor('mu_BR_tautau', 1., 0., 200., True)

        #mu_XS[energy]_[mode]
        #_, (xs_up, xs_down) = yellowhiggs.xs(
        #    energy, self.mass, self.MODES_DICT[self.mode][0],
        #    error_type='factor')
        #sample.AddOverallSys(
        #    'mu_XS{0:d}_{1}'.format(energy, self.MODES_WORKSPACE[self.mode]),
        #    xs_down, xs_up)
        sample.AddNormFactor(
            'mu_XS{0:d}_{1}'.format(energy, self.MODES_WORKSPACE[self.mode]),
            1., 0., 200., True)

        # https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/HSG4Uncertainties
        # pdf uncertainty
        if mode == 'gg':
            if energy == 8:
                sample.AddOverallSys('pdf_Higgs_gg', 0.93, 1.08)
            else: # 7 TeV
                sample.AddOverallSys('pdf_Higgs_gg', 0.92, 1.08)
        else:
            if energy == 8:
                sample.AddOverallSys('pdf_Higgs_qq', 0.97, 1.03)
            else: # 7 TeV
                sample.AddOverallSys('pdf_Higgs_qq', 0.98, 1.03)

        # EWK NLO CORRECTION FOR VBF ONLY
        if mode == 'VBF':
            sample.AddOverallSys('NLO_EW_Higgs', 0.98, 1.02)

        # QCDscale_ggH3in HistoSys ONLY FOR MVA
        # also see ggH3in script
        if mva and mode == 'gg' and category.name == 'vbf' and self.channel=='hadhad':
            Rel_Error_2j = 0.215
            Error_exc = 0.08613046469238815 # Abs error on the exclusive xsec
            xsec_exc = 0.114866523583739 # Exclusive Xsec
            Error_3j = sqrt(Error_exc**2 - (Rel_Error_2j*xsec_exc)**2)
            rel_error = Error_3j / xsec_exc

            dphi = rec['true_dphi_jj_higgs_no_overlap']
            scores = rec['classifier']

            idx_2j = ((pi - dphi) < 0.2) & (dphi >= 0)
            idx_3j = ((pi - dphi) >= 0.2) & (dphi >= 0)

            # get normalization factor
            dphi_2j = weights[idx_2j].sum()
            dphi_3j = weights[idx_3j].sum()

            weight_up = np.ones(len(weights))
            weight_dn = np.ones(len(weights))

            weight_up[idx_2j] -= (dphi_3j / dphi_2j) * rel_error
            weight_dn[idx_2j] += (dphi_3j / dphi_2j) * rel_error

            weight_up[idx_3j] += rel_error
            weight_dn[idx_3j] -= rel_error

            weight_up *= weights
            weight_dn *= weights

            up_hist = nominal.clone(shallow=True, name=sample_nom.name + '_QCDscale_ggH3in_UP')
            up_hist.Reset()
            dn_hist = nominal.clone(shallow=True, name=sample_nom.name + '_QCDscale_ggH3in_DOWN')
            dn_hist.Reset()

            fill_hist(up_hist, scores, weight_up)
            fill_hist(dn_hist, scores, weight_dn)

            if uniform:
                up_hist = uniform_hist(up_hist)
                dn_hist = uniform_hist(dn_hist)

            shape = histfactory.HistoSys('QCDscale_ggH3in',
                low=dn_hist,
                high=up_hist)
            norm, shape = histfactory.split_norm_shape(shape, sample_nom)
            sample.AddHistoSys(shape)

    def xsec_kfact_effic(self, isample):
        # use yellowhiggs for cross sections
        xs, _ = yellowhiggs.xsbr(
            self.energy, self.masses[isample],
            Higgs.MODES_DICT[self.modes[isample]][0], 'tautau')
        log.debug("{0} {1} {2} {3} {4} {5}".format(
            self.samples[isample],
            self.masses[isample],
            self.modes[isample],
            Higgs.MODES_DICT[self.modes[isample]][0],
            self.energy,
            xs))
        if not self.inclusive_decays:
            xs *= TAUTAUHADHADBR
        kfact = 1.
        effic = 1.
        return xs, kfact, effic


class InclusiveHiggs(MC, Signal):
    # for overlap study
    SAMPLES = {
        'ggf': 'PowPyth8_AU2CT10_ggH125p5_inclusive.mc12b',
        'vbf': 'PowPyth8_AU2CT10_VBFH125p5_inclusive.mc12b',
        'zh': 'Pyth8_AU2CTEQ6L1_ZH125p5_inclusive.mc12b',
        'wh': 'Pyth8_AU2CTEQ6L1_WH125p5_inclusive.mc12b',
        'tth': 'Pyth8_AU2CTEQ6L1_ttH125p5_inclusive.mc12b',
    }

    def __init__(self, mode=None, **kwargs):
        self.energy = 8
        if mode is not None:
            self.modes = [mode]
            self.masses = [125]
            self.samples = [self.SAMPLES[mode]]
        else:
            self.masses = [125] * 5
            self.modes = ['ggf', 'vbf', 'zh', 'wh', 'tth']
            self.samples = [
                'PowPyth8_AU2CT10_ggH125p5_inclusive.mc12b',
                'PowPyth8_AU2CT10_VBFH125p5_inclusive.mc12b',
                'Pyth8_AU2CTEQ6L1_ZH125p5_inclusive.mc12b',
                'Pyth8_AU2CTEQ6L1_WH125p5_inclusive.mc12b',
                'Pyth8_AU2CTEQ6L1_ttH125p5_inclusive.mc12b',
            ]
        super(InclusiveHiggs, self).__init__(
            year=2012, name='Signal', label='Signal',
            ntuple_path='ntuples/prod_v29',
            student='hhskim_overlap',
            **kwargs)

    def xsec_kfact_effic(self, isample):
        # use yellowhiggs for cross sections
        xs, _ = yellowhiggs.xs(
            self.energy, self.masses[isample], self.modes[isample])
        log.debug("{0} {1} {2} {3} {4}".format(
            self.samples[isample],
            self.masses[isample],
            self.modes[isample],
            self.energy,
            xs))
        kfact = 1.
        effic = 1.
        return xs, kfact, effic
