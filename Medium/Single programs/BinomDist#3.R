cat(sprintf("%.3f",dbinom(0, size=10, prob=0.12)+dbinom(1, size=10, prob=0.12)+
              dbinom(2, size=10, prob=0.12) ))

cat(sprintf("\n%.3f",1-dbinom(0, size=10, prob=0.12)-dbinom(1, size=10, prob=0.12) ))
