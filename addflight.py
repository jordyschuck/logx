import streamlit as st
from datetime import date
from helpers import insertFlight

def app():
    st.title("Add Flight")
    st.subheader("Log a New Flight")

    with st.form("logForm"):
        with st.container(border=True):
            st.subheader("Basic Information")
            flightDate = st.date_input("Date", value=date.today())
            reg = st.text_input("Tail Number")
            fromField = st.text_input("Departure")
            toField = st.text_input("Arrival Field")

        with st.container(border=True):
            st.subheader("Times")
            totalTime = st.number_input("Total Time")
            pic = st.number_input("PIC Time")
            sic = st.number_input("SIC Time")
            solo = st.number_input("Solo Time")
            multi = st.number_input("Multi Time")
            night = st.number_input("Night Time")
            xc = st.number_input("Cross-Country Time")
            sim = st.number_input("Time in a Simulator (FTD)")

        with st.container(border=True):
            st.subheader("FAR Requirements")
            dayTo = st.number_input("Day Takeoffs", step=1)
            dayLandings = st.number_input("Day Landings Full-Stop", step=1)
            nightTo = st.number_input("Night Takeoffs", step=1)
            nightLandings = st.number_input("Night Landings Full-Stop", step=1)
            allLandings = st.number_input("All Landings", step=1)

        with st.container(border=True):
            st.subheader("IFR")
            hoodTime = st.number_input("Simulated IMC")
            hardIMC = st.number_input("Real IMC Time")
            holds = st.number_input("Holds", step=1)
            approaches = st.number_input("Approaches", step=1)

        with st.container(border=True):
            st.subheader("Cross Country")
            via = st.text_input("Via Route (Between From and To)")
            xcdist = st.number_input("Distance of route total")

        with st.container(border=True):
            st.subheader("NVG Ops")
            nvg = st.number_input("Time with NVGs")
            nvgOps = st.number_input("Number of ops with the NVGs", step=1)

        with st.container(border=True):
            st.subheader("Instruction")
            dualGiven = st.number_input("Time for Dual Given")
            dualReceived = st.number_input("Time for Dual Received")
            groundGiven = st.number_input("Ground Time Given")
            groundReceived = st.number_input("Ground Time Received")

        with st.container(border=True):
            st.subheader("Signatures")
            signature = st.text_input("Endorse Here PIC")
            signatureCFI = st.text_input("CFI Endorsement Here")
            signing = f"{signature} | {signatureCFI}"

        submitted = st.form_submit_button("Submit")

    if submitted:
        entry = {
            "date": str(flightDate),
            "tail": reg,
            "dep": fromField,
            "arr": toField,
            "via": via,
            "totaltime": totalTime,
            "pic": pic,
            "sic": sic,
            "multi": multi,
            "night": night,
            "solo": solo,
            "xc": xc,
            "approaches": approaches,
            "xcdist": xcdist,
            "dayto": dayTo,
            "daylndstop": dayLandings,
            "nightto": nightTo,
            "nightlndstop": nightLandings,
            "alllandings": allLandings,
            "hardimc": hardIMC,
            "hoodsim": hoodTime,
            "holds": holds,
            "nvg": nvg,
            "nvgops": nvgOps,
            "dualgiven": dualGiven,
            "dualreceived": dualReceived,
            "simulated": sim,
            "ground": groundReceived,
            "groundgiven": groundGiven,
            "signing": signing
        }

        insertFlight(entry)
        st.success("✅ Flight successfully logged.")
