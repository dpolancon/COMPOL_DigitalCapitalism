import os

# Create new folder
new_folder = "06_drafts"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    print(f"Created folder: {new_folder}")
else:
    print(f"Folder already exists: {new_folder}")

# Create new file
new_file = "v1_systematic_review_draft.md"
file_path = os.path.join(new_folder, new_file)

# Write content to file
content = """# Systematic Review: Financialization and Land Rent

## Introduction
Financialization has been linked to an increase in land rent, which has negative consequences for the economy. This review aims to examine the relationship between financialization and land rent.

## Method and Corpus
This review will cover the literature on financialization and land rent from 2000 to 2022. The corpus will include academic articles, books, and reports.

## Conceptual Foundations
Financialization refers to the increasing importance of financial markets and institutions in the economy. Land rent, on the other hand, refers to the income earned by landowners from the use of their land.

## Land-Price Inflation and Capital-Formation Crowding-Out
Financialization has led to an increase in land prices, which has crowded out capital formation in other sectors of the economy.

## Credit, Collateral, Leverage, and Monetary Policy
The use of credit, collateral, and leverage has contributed to the increase in land prices. Monetary policy has also played a role in the financialization of land.

## Unbalanced Growth and the Land Overvaluation Theorem
The financialization of land has led to unbalanced growth, with some sectors of the economy growing faster than others. The land overvaluation theorem suggests that this can lead to a bubble in the land market.

## R versus G and Infinite Debt Rollover
The relationship between the interest rate (R) and the growth rate (G) is crucial in determining the sustainability of debt. If R is greater than G, debt rollover can become infinite, leading to a debt crisis.

## Policy Implications
Policy makers should be aware of the risks associated with financialization and take steps to mitigate them. This can include implementing policies to reduce the use of credit, collateral, and leverage, as well as implementing monetary policies that promote balanced growth.

## Critical Appraisal and Fondecyt Translation
This review has provided a critical appraisal of the literature on financialization and land rent. The findings of this review can be translated into Spanish to reach a wider audience.

## Conclusion
In conclusion, financialization has led to an increase in land rent, which has negative consequences for the economy. Policy makers should be aware of the risks associated with financialization and take steps to mitigate them.

## References

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]


# Citation Audit

## Introduction
This citation audit aims to examine the citations used in this systematic review.

## Method and Corpus
This citation audit will cover all the citations used in this systematic review.

## Results

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]

## Discussion

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]

## Conclusion

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]


# Draft Pass Audit Report

## Introduction
This draft pass audit report aims to examine the draft of this systematic review.

## Method and Corpus
This draft pass audit report will cover the draft of this systematic review.

## Results

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]

## Discussion

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]

## Conclusion

* [PAGE NEEDED]
* [VALIDATION NEEDED]
* [SOURCE RELATION CHECK]
"""

with open(file_path, "w") as f:
    f.write(content)
    print(f"Created file: {file_path}")

print("Done!")