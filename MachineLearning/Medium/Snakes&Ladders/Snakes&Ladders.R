#filename <- file("stdin")
#open(filename)

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
  Mladders=matrix(unlist(strsplit(unlist(strsplit(inputline,split=" ")),split=",")),ncol=2,byrow = TRUE)
  ladders=c(as.numeric(Mladders[,2]))
  names(ladders)=c(as.numeric(Mladders[,1]))
  #snakes coords
  inputline=readLines(filename,n=1)
  Msnakes=matrix(unlist(strsplit(unlist(strsplit(inputline,split=" ")),split=",")),ncol=2,byrow = TRUE)
  snakes=c(as.numeric(Msnakes[,2]))
  names(snakes)=c(as.numeric(Msnakes[,1]))  
  #play game 5000 times
  total=0
  for (j in 1:5000){
    n=0 #amount of throws
    cur=1 #current position
    while (cur<100){
      x=as.numeric(sample(dicelist[,2],size=1,prob=dicelist[,1]))
      n=n+1
      if ((cur+x)<=100){
        cur=cur+x
        #check if ladder
        ladder=as.numeric(ladders[toString(cur)])
        if (!is.na(ladder)){cur=ladder}
        #check if snake
        snake=as.numeric(snakes[toString(cur)])
        if (!is.na(snake)){cur=snake}
      }
    }
    total=total+n
  }
  cat(sprintf("%0.f\n",total/5000))
}

close(filename)