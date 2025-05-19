import streamlit as st
from helpers import getAllFlights

def app():
    st.title("All Logged Flights")
    df = getAllFlights()

    if df.empty:
        st.info("No Flights Found")
        return
    
    st.subheader(f"{len(df)} flights logged")

    for i, row in df.iterrows():
        with st.container(border = True):
            st.markdown(f"**Date:** {row['date']} // ** Tail** {row['tail']}") 
            st.write({
                            "From": row["dep"],
                            "To": row["arr"],
                            "Via": row["via"],
                            "Time": row["totaltime"],
                            "PIC": row["pic"],
                            "SIC": row["sic"],
                            "Night": row["night"],
                            "Landings": row["alllandings"],
                            "Approaches": row["approaches"],
                            "Signature": row["signing"]
                        })