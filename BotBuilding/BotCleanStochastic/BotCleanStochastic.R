# Enter your code here. Read input from STDIN. Print output to STDOUT

inputset <- read.table("H:/R/Hackerrank/BotBuilding/BotCleanStochastic/input.txt",header=FALSE,sep="@",stringsAsFactors=FALSE)
#inputset <- read.table("stdin",header=FALSE,sep="@",stringsAsFactors=FALSE)
startbot=c(as.numeric(substr(inputset[1,],1,1))+1,as.numeric(substr(inputset[1,],3,3))+1)
msize= 5
for (i in 1:msize){
  for (j in 1:msize){
    cchar=substr(inputset[(i+1),],j,j)
    if (cchar=="b"){
      bot=c(i,j)
    }
    if (cchar=="d" & !exists("dirt")){
      dirt=c(i,j)
    }
  }
}
if (!exists("bot")){
  cat("CLEAN\n")
}else{
  if (dirt[1]!=bot[1]){
    if (dirt[1]>bot[1]){
      cat("DOWN\n")
      bot[1]=bot[1]+1
    }else{
      cat("UP\n")
      bot[1]=bot[1]-1
    }
  }else{
    if (dirt[2]!=bot[2]){
      if (dirt[2]>bot[2]){
        cat("RIGHT\n")
        bot[2]=bot[2]+1
      }else{
        cat("LEFT\n")
        bot[2]=bot[2]-1
      }
    }
  }
}