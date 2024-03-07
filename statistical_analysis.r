library(readr)

# Explicitly specify the delimiter
data <- read.csv("/Users/clairesuen/Desktop/data.csv")

# Check the first few rows of the data
head(data)

t_test_result <- t.test(Distance ~ Age, data = data)

# Print the results
print(t_test_result)



data$Age_Group <- as.factor(data$Age_Group)

model <- lm(Distance ~ Age + Gender, data = data)
summary_result <- summary(model)
anova_result <- anova(model)
# Display the ANOVA table
print(summary_result)
print(anova_result)




model2 <- lm(Distance ~ Age, data = data)
summary_result2 <- summary(model2)
anova_result2 <- anova(model2)
print(summary_result2)
print(anova_result2)


data$binary <- ifelse(data$Age_Group %in% c("Adult", "Elderly"), 0, 
                      ifelse(data$Age_Group %in% c("Infant", "Juvenile"), 1, NA))

model3 <- lm(Distance ~ binary + Gender, data = data)
summary_result3 <- summary(model3)
anova_result3 <- anova(model3)
print(summary_result3)
print(anova_result3)

