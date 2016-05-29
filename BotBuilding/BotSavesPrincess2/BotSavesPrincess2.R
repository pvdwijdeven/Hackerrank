# Enter your code here. Read input from STDIN. Print output to STDOUT

inputset <- read.table("H:/R/Hackerrank/BotBuilding/BotSavesPrincess2/input.txt",header=FALSE,sep="@",stringsAsFactors=FALSE)
#inputset <- read.table("stdin",header=FALSE,sep="@",stringsAsFactors=FALSE)

msize= as.numeric(inputset[1,])
for (i in 1:msize){
  for (j in 1:msize){
    cchar=substr(inputset[(i+2),],j,j)
    if (cchar=="m"){
      mario=c(i,j)
    }
    if (cchar=="p"){
      princess=c(i,j)
    }
  }
}

if (princess[1]!=mario[1]){
  if (princess[1]>mario[1]){
    cat("DOWN\n")
    mario[1]=mario[1]+1
  }else{
    cat("UP\n")
    mario[1]=mario[1]-1
  }
}else{
  if (princess[2]!=mario[2]){
    if (princess[2]>mario[2]){
      cat("RIGHT\n")
      mario[2]=mario[2]+1
    }else{
      cat("LEFT\n")
      mario[2]=mario[2]-1
    }
  }
}