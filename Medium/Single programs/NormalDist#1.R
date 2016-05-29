cat(sprintf("%.3f",pnorm(19.5, mean=20, sd=2, lower.tail=TRUE) ))
cat(sprintf("\n%.3f",pnorm(22, mean=20, sd=2, lower.tail=TRUE)-pnorm(20, mean=20, sd=2, lower.tail=TRUE) ))
