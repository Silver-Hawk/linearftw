# PRIMAL:
#   max     x1 + 2  x2
#       −2  x1 - 1  x2 ≤ −3
#       −1  x1 + 3  x2 ≤ 24
#       1   x1 − 1  x2 ≤ 6
#       2   x1 + 1  x2 ≤ 29

# pretty print
print.matrix <- function(m){
  write.table(format(m, justify="right"),
              row.names=F, col.names=F, quote=F)
}


A <- matrix(c(-2,-1,
              -1, 3,
               1, 1,
               2, 1),byrow = T,ncol = 2)

b <- matrix(c(-3,24,6,29),byrow = T, ncol = 1)

c <- matrix(c(1,2),byrow = T,ncol = 2)

print(rbind(t(c(b,NA)),cbind(t(A),t(c))))

