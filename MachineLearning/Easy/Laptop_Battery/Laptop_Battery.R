data <- read.table("trainingdata.txt",header=FALSE,sep=",")
charged <- data$V1
lasted <- data$V2
full <- charged>4
myfit <- lm(lasted~charged*full+full)
test.input=readLines(file("stdin"))
pred.input = data.frame(charged = as.numeric(test.input),full=as.numeric(test.input)>4)
result <- predict(myfit,pred.input)
cat(sprintf("%f", result))