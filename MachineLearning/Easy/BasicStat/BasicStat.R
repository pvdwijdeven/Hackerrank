

inputset <- read.csv("H:/R/Hackerrank/Easy/BasicStat/input.txt",header=FALSE,sep=" ")
#inputset <- read.csv(file("stdin"),header=FALSE,sep=" ")
Mode <- function(x) {
  temp=table(x)
  min(as.numeric(names(temp)[temp == max(temp)]))
}
count=inputset[1,1]
inputVector=c(unlist(inputset[2,1:count]))

#var and sd are based on sample, so count-1. In this case count is asked in stead.
sd = sqrt(var(inputVector)*(count-1)/count)

cat(sprintf("%.1f\n", mean(inputVector)))
cat(sprintf("%.1f\n", median(inputVector)))
cat(sprintf("%.0f\n", Mode(inputVector)))
cat(sprintf("%.1f\n",sd))
cat(sprintf("%.1f ",mean(inputVector)-1.96*sd/sqrt(count)))
cat(sprintf("%.1f",mean(inputVector)+1.96*sd/sqrt(count)))
