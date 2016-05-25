inputset <- read.csv("H:/R/Hackerrank/Easy/PolReg/Input.txt",header=FALSE,sep=" ")
#inputset <- read.csv(file("stdin"),header=FALSE,sep=" ")
FF=inputset[1,1]
NN=inputset[1,2]
TT=inputset[(NN+2),1]
Train.X=matrix(unlist(inputset[2:(NN+1),1:FF]),ncol=FF,byrow=FALSE)
Train.Y=matrix(unlist(inputset[2:(NN+1),FF+1]), ncol=1,byrow=FALSE)
Test.X=matrix(unlist(inputset[(NN+3):(NN+2+TT),1:FF]),ncol=FF,byrow=FALSE)
myfit=lm(Train.Y~.,data=data.frame(poly(Train.X,degree=3,raw=TRUE)))
result=predict(myfit,data.frame(poly(Test.X,degree=3,raw=TRUE)),interval="none",type="response")
cat(sprintf("%f", result),sep="\n")