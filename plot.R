rm(list=ls())

# Load all necessary libraries
install.packages("ggplot2")
install.packages("dplyr")
install.packages("ggpubr")
install.packages("dplyr")
install.packages("readxl")

library(readxl)
library(ggplot2) 
library(dplyr)
library(ggpubr)
theme_set(theme_pubr())


getwd(); 
#setwd("/Users/vlipari/Documents/DSMM/R")
data = read_excel('textmining.xlsx')


# 1. Recommended IND - Number of Reviewers by Recommended IND ####

data %>% 
  group_by(Age, `Recommended IND`) %>% 
  summarise(N=n(), recommended = as.factor(round(mean(`Recommended IND`)))) %>%
ggplot(aes(x=Age,y=N, col=recommended)) +
  geom_point() +
  geom_smooth(method = "lm")


# 2. Ratings - Number of Reviewers by Rating ###

data %>% 
  group_by(Age, Rating) %>% 
  summarise(N=n(), rating = as.factor(mean(Rating))) %>% 
ggplot(aes(x=Age,y=N, col=rating)) +
  geom_point() +
  geom_smooth(method = "lm")

# 3. Positive Feedback - Number of Reviewers by Positive Feedback ####

data$positiveCount <- cut(data$`Positive Feedback Count`, breaks = c(0,30,60,90,120), labels = c("(0-30)","(31-60)",
                                                                    "(61-90)","(91-120)"))
data %>% 
  group_by(Age, `Positive Feedback Count`) %>% 
  summarise(N=n(), feedback = as.factor(mean(`Positive Feedback Count`))) %>% 
  ggplot(aes(x=Age,y=N, col=feedback)) +
  geom_point() +
  geom_smooth(method = "lm")

# 4. Positive Feedback - Number of Reviewers by Positive Feedback ####


ll <- data.frame(table(data$`Clothing ID`))
dataFreq <- arrange(ll, desc(ll$Freq))
freq_groups <- dataFreq %>% select(Var1,Freq) %>% group_by(Freq)
for (d in 1:nrow(freq_groups)){
  perc <- freq_groups$Freq/length(data$`Clothing ID`)*100
}
dataFreq$Percentage <- perc
freq_groups <- dataFreq %>% select(Var1,Freq,Percentage) %>% group_by(Percentage) 

# 5. Clothing Id - Density of Clothing Id ####

x <- data$`Clothing ID`
plot(density(x),                              
main = "Density",
xlab = "Clothing Id",
ylab = "Density of Clothing Id")

polygon(density(x), col = "#1b98e0")

#hist(x, prob = TRUE)                                

#h <- hist(x,ylim=c(0,10000))

# 6. Frequency - Frequency of Clothing ID ####

ggscatter(freq_groups, x = "Var1", y = "Freq", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Clothing Id", ylab = "Frequency", col = "#1b98e0") 

# 7. Percentage of frequency distribution ####

ggscatter(freq_groups, x = "Var1", y = "Percentage", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Clothing Id", ylab = "Frequency", col = "#1b98e0") 

freq_head <- head(freq_groups,15)

df.data <- data.frame("x" = freq_head$Freq, "y" = freq_head$Var1, "group" = freq_head$Freq) 
ggplot(data = df.data) + 
  geom_point(aes(x = freq_head$Freq, y = y, colour = group)) 
