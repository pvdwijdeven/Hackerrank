inputset <- read.csv("H:/R/Hackerrank/Easy/Stock_Predictions/input.txt",header=FALSE,sep=" ")
#inputset <- read.csv(file("stdin"),header=FALSE,sep=" ")

# 1st attempt: focus on 1st stock: sell if higher than yesterday, buy if lower than yesterday
# 2nd: same for all stocks, pick highest gain/loss
# 3rd: pick percentage << works worse than 2nd
# 4th: linear regression on current dataset
# future attempts:
# 5th: linear regression on histyory
# 6th: same for other algorithms
# 7th: train on test data



money=inputset[1,1]
money=as.numeric(as.character(money))#factorized due to text in same column
stocks_available=as.numeric(inputset[1,2])
days_remaining=as.numeric(inputset[1,3])
Stocks=(data.frame(inputset[2:(stocks_available+1),]))
Buysell=data.frame(Name="STOCK",BS="BUY/SELL",Amount=0,stringsAsFactors=FALSE)

ScanStocks=Stocks
counter=1
ScanStocks=cbind(ScanStocks,abs(ScanStocks[,6]-ScanStocks[,7]))
while (dim(ScanStocks)[1]>0) {
  
  #search biggest relative difference (min or max(yest-tod))
  focus=which.max(ScanStocks[,8])# SELL first
  if(as.numeric(ScanStocks[focus,6])>as.numeric(ScanStocks[focus,7]))
  {focus=which.max(ScanStocks[,8])}# now BUY
  #write.table(ScanStocks[focus,],row.names=F,col.names=F)
  Buysell[counter,1]=as.character(ScanStocks[focus,1])
  if(as.numeric(ScanStocks[focus,6])>as.numeric(ScanStocks[focus,7])){
    #Price dropped, buy
    Buysell[counter,2]='BUY'
    Buysell[counter,3]=floor(money/as.numeric(ScanStocks[focus,7]))
    money=money-Buysell[counter,3]*as.numeric(ScanStocks[focus,7])
  }else{
    #Price raised, sell
    Buysell[counter,2]='SELL'
    Buysell[counter,3]=as.numeric(ScanStocks[focus,2])
  }
  #quick fix: only BUY/SELL when this is 2nd day of asc/desc:
  if (Buysell[counter,2]=='BUY'){
    if(as.numeric(ScanStocks[focus,5])<as.numeric(ScanStocks[focus,6])){
      #Buysell[counter,3]=0
    }
  }else{
    if(as.numeric(ScanStocks[focus,5])>as.numeric(ScanStocks[focus,6])){
      #Buysell[counter,3]=0
    }
  }
  
  # write.table(Buysell,col.names=F,row.names=F)
  if (Buysell[counter,3]!=0){counter=counter+1}else{Buysell=Buysell[-counter,]}
  ScanStocks=ScanStocks[-focus,]
}

counter=counter-1
if (counter==0){
  cat("0\n")
}else{
  cat("1\n")
  write.table(Buysell,row.names=FALSE,col.names=FALSE,quote=FALSE)
}

