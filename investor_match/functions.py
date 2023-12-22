def investor_matching(loan, investor_guidelines):
    matches = []  # List to store matches and scores
    
    for investor, guidelines in investor_guidelines.items():
        score = calculate_match_score(loan, guidelines)
        matches.append((investor, score))

    # Sort the matches based on score in descending order
    matches.sort(key=lambda x: x[1], reverse=True)

    # Return the top 3 matches and their scores
    return matches[:3]

def calculate_match_score(loan, investor_guidelines):
    score = 0
    
    # Extract relevant loan components
    ltv = loan['LTV']
    credit_score = loan['CreditScore']
    transaction_history = loan['TransactionHistory']
    loan_type = loan['LoanType']
    
    # Extract investor-specific guidelines
    ltv_min = investor_guidelines.get('LTV_min', 0)
    ltv_max = investor_guidelines.get('LTV_max', 1)
    credit_score_min = investor_guidelines.get('CreditScore_min', 0)
    transaction_history_min = investor_guidelines.get('TransactionHistory_min', 0)

    
    # Calculate a score based on how closely the loan matches the investor's criteria
    # You can assign different weights to each criteria based on importance
    if ltv_min <= ltv <= ltv_max:
        score += 1
    
    if credit_score >= credit_score_min:
        score += 1
    
    if transaction_history >= transaction_history_min:
        score += 1
    
    # Add more scoring logic based on other investor guidelines
    
    # Example: Give extra score if loan type matches
    if loan_type == investor_guidelines.get('LoanType', ''):
        score += 1

    return score
