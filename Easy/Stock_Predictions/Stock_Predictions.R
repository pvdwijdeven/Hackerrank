inputset <- read.csv("H:/R/Hackerrank/Easy/Stock_Predictions/input.txt",header=FALSE,sep=" ")
#inputset <- read.csv(file("stdin"),header=FALSE,sep=" ")

# 1st attempt: focus on 1st stock: sell if higher than yesterday, buy if lower than yesterday
# future attempts:
# 2nd: same for all stocks, pick highest/lowest
# 3rd: pick percentage
# 4th: linear regression on current dataset
# 5th: linear regression on histyory
# 6th: same for other algorithms
# 7th: train on test data

money=inputset[1,1]
money=as.numeric(as.character(money))
stocks_available=as.numeric(inputset[1,2])
days_remaining=as.numeric(inputset[1,3])
Stocks=(data.frame(inputset[2:(stocks_available+1),]))
Buysell=data.frame(Name=character(),BS=character(),Amount=integer(),stringsAsFactors=FALSE)

Buysell[1,1]=as.character(Stocks[1,1])
if(as.numeric(Stocks[2,6])>as.numeric(Stocks[2,7])){
  #Price dropped, buy
  Buysell[1,2]='BUY'
  Buysell[1,3]=floor(money/as.numeric(Stocks[2,7]))
  }else{
    #Price raised, sell
    Buysell[1,2]='SELL'
    Buysell[1,3]=as.numeric(Stocks[2,2])
}

result=Buysell
cat("1\n")
cat(sprintf("%s", result),sep=" ")