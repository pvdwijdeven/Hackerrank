Physics.Scores=c(15,12,8,8,7,7,7,6,5,3)
History.Scores=c(10,25,17,11,13,17,20,13,9,15)
Scores=matrix(Physics.Scores)
Scores=cbind(Scores,History.Scores)
result=coef(lm(History.Scores~Physics.Scores))[2]
 
cat(sprintf("%.3f", result ))
