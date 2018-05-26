#include <iostream>

float GetTopPtWeight(float truth_top0_pt){
  float  top_pt_weight=1;
  
  if(truth_top0_pt > 1 && truth_top0_pt < 45e3) top_pt_weight = 1.06543; //<! truth_top0_pt is 0 for non top samples
  if(truth_top0_pt>45e3&&truth_top0_pt<90e3)top_pt_weight = 1.02734;
  if(truth_top0_pt>90e3&&truth_top0_pt<135e3)top_pt_weight = 0.995909;
  if(truth_top0_pt>135e3&&truth_top0_pt<180e3)top_pt_weight = 0.976004;
  if(truth_top0_pt>180e3&&truth_top0_pt<225e3)top_pt_weight = 0.960986;
  if(truth_top0_pt>225e3&&truth_top0_pt<270e3)top_pt_weight = 0.948039;
  if(truth_top0_pt>270e3&&truth_top0_pt<315e3)top_pt_weight = 0.936764;
  if(truth_top0_pt>315e3&&truth_top0_pt<400e3)top_pt_weight = 0.917721;
  if(truth_top0_pt>400e3&&truth_top0_pt<800e3)top_pt_weight = 0.867114;
  
  return top_pt_weight;
}
