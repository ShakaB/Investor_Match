import streamlit as st
from functions import investor_matching, calculate_match_score
from investors import investor_guidelines



def main():
    st.title("Investor Matching App")

    # Define loan inputs using Streamlit widgets
    loan_ltv = st.slider("Loan-to-Value Ratio (LTV)", 0.0, 1.0, 0.75, 0.01)
    loan_credit_score = st.number_input("Credit Score", value=720)
    loan_transaction_history = st.number_input("Transaction History", value=2)
    loan_type = st.selectbox("Loan Type", ["Bridge", "Long Term", '30-year'])

    loan = {
        'LTV': loan_ltv,
        'CreditScore': loan_credit_score,
        'TransactionHistory': loan_transaction_history,
        'LoanType': loan_type
    }

    top_matches = investor_matching(loan, investor_guidelines)

    # Display results for the top 3 matches
    st.subheader("Top 3 Investor Matches:")
    for i, (investor, score) in enumerate(top_matches):
        st.write(f"Rank {i + 1}: Investor: {investor}, Match Score: {score}")

    if not top_matches:
        st.subheader("No suitable investor found.")

if __name__ == "__main__":
    main()