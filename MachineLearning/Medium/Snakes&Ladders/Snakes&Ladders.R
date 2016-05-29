#filename <- file("stdin")

filename <- file("H:/R/Hackerrank/MachineLearning/Medium/Snakes&Ladders/input.txt", "r")
ntests=as.numeric(readLines(filename,n=1))
for (i in 1:3){
  #dicelist
  inputline=readLines(filename,n=1)
  dicelist=matrix(unlist(strsplit(inputline,split=",")))
  dicelist=cbind(dicelist,c(1:6))
  #Number of snakes & ladders, not used
  inputline=readLines(filename,n=1)
  #ladders coords
  inputline=readLines(filename,n=1)
  ladders=matrix(unlist(strsplit(unlist(strsplit(inputline,split=" ")),split=",")),ncol=2,byrow = TRUE)
  #snakes coords
  inputline=readLines(filename,n=1)
  snakes=matrix(unlist(strsplit(unlist(strsplit(inputline,split=" ")),split=",")),ncol=2,byrow = TRUE)
  
  #play game 5000 times
  total=0
  for (j in 1:500){
    n=0 #amount of throws
    cur=1 #current position
    while (cur<100){
      x=as.numeric(sample(dicelist[,2],size=1,prob=dicelist[,1]))
      n=n+1
      if ((cur+x)<=100){
        cur=cur+x
        #check if ladder
        if (length(which(ladders==x))){
          if (which(ladders==x)<=dim(ladders)[1]){
            cur=as.numeric(ladders[dim(ladders)[1]+which(ladders==x)])
          }
        }
        #check if snake
        if (length(which(snakes==x))){
          if (which(snakes==x)<=dim(snakes)[1]){
            cur=as.numeric(snakes[dim(snakes)[1]+which(snakes==x)])
          }
        }
      }
    }
    total=total+n
  }
  cat(sprintf("%0.f\n",total/500))
}

close(filename)