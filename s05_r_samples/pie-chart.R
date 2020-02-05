# Title     : demo
# Objective : demo
# Created by: jetbrains
# Created on: 20/09/2019

# Simple Pie Chart
slices <- c(10, 12, 4, 16, 10)
lbls <- c("US", "UK", "Australia", "Germany", "France")
mytable <- (slices)
pie(slices, labels = lbls, main = "Pie Chart of Countries")