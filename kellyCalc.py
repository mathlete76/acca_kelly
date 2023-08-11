import streamlit as st

st.header("Acca Stake Calculator")

frac = 0.25
bookOdds = st.number_input('Acca Odds: ', min_value=float(1.0), help="Use Decimal Odds")
adjustedOdds = 10 * bookOdds / 6
fairOdds = st.number_input('Fair Odds: ', min_value=(1.0), help="Use Decimal Odds")
bankRoll = st.number_input('Bankroll: ')

if bankRoll != 0:
    stake = bankRoll * frac * (((1/fairOdds)*adjustedOdds)-1)/(adjustedOdds-1)
else:
    stake = 0

if stake > 0:
    st.subheader("Suggested Stake")
    st.text(f"The optimal stake for this bet is {stake:.2f}")
elif stake <0:
    st.subheader("Suggested Stake")
    st.text(f"This is not a value bet.")
else:
    st.subheader("Awaiting inputs...")