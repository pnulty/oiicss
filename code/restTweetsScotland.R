#!/usr/bin/Rscript
library('twitteR')
setup_twitter_oauth('ZOHJIRAwnw23FhvFWyUg','HTfEcEmRRDcx0ZsJ5CHOcmPc84AfDOp5VvIXwt0oY','778251283-ZkDTfl3IbIFZFXlVokA6Gpc19TZPyov3wucZ0XaB','8vgPnpEWP3qhvILmTLXVb9RslwcEwVVeKOo4KCYHOY')

scotResults1409 <- data.frame()
sea <- searchTwitter('indyref OR salmond OR cameron OR scotland OR scottish OR referendum OR vote OR voted OR voting', n=1000, since='2014-09-14', until='2014-09-15')
newResults <- twListToDF(sea)
y <- tail(newResults,1)
i <- 0
while(i < 700){
  print(i)
  y <- tail(newResults)
  scotResults1409  <-  rbind(scotResults1409, newResults)
  sea <- searchTwitter('indyref OR salmond OR cameron OR scotland OR scottish OR referendum OR vote OR voted OR voting', n=1000, lang='en', since='2014-09-14', until='2014-09-15', maxID=y[1,8])
  newResults <- twListToDF(sea)
  print(nrow(newResults))
  print(nrow(scotResults1409))
  print(y[6,5])
  print('sleeping\n')
  Sys.sleep(70)
  i <- i+1
  scotResults1409 <- scotResults1409[scotResults1409$isRetweet==FALSE, ]
  save(scotResults1409, file='~/backup/R1409backup.RData')
}
save(scotResults1409, file='~/backup/R1409backup.RData')
#save(scotResults1409, file='~/Dropbox/oiicss/data/scotResults1409.RData')






