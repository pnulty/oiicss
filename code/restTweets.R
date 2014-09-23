library('twitteR')
setup_twitter_oauth('ZOHJIRAwnw23FhvFWyUg','HTfEcEmRRDcx0ZsJ5CHOcmPc84AfDOp5VvIXwt0oY','778251283-ZkDTfl3IbIFZFXlVokA6Gpc19TZPyov3wucZ0XaB','8vgPnpEWP3qhvILmTLXVb9RslwcEwVVeKOo4KCYHOY')

allResults <- data.frame()
sea <- searchTwitter('indyref OR salmond OR cameron OR scotland', n=1000)
setup_twitter_oauth('ZOHJIRAwnw23FhvFWyUg','HTfEcEmRRDcx0ZsJ5CHOcmPc84AfDOp5VvIXwt0oY','778251283-ZkDTfl3IbIFZFXlVokA6Gpc19TZPyov3wucZ0XaB','8vgPnpEWP3qhvILmTLXVb9RslwcEwVVeKOo4KCYHOY')

newResults <- twListToDF(sea)
us <- getUser(newResults$screenName[[2]])
y <- tail(newResults,1)
i <- 0
while(i < 100){
  y <- tail(newResults)
  allResults  <-  rbind(allResults, newResults)
  sea <- searchTwitter('immigrants OR immigrant OR immigration OR immigrate', n=1000, lang='en', since='2014-05-22', until='2014-05-23',maxID=y[1,8])
  newResults <- twListToDF(sea)
  print(nrow(newResults))
  print(nrow(allResults))
  print(y[6,5])
  print('sleeping\n')
  Sys.sleep(90)
  i <- i+1
  
}
save(allResults, file='results.RData')






