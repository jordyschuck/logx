import streamlit as st
import sqlite3 as sq
import pandas as pd

def init_db():
    conn = sq.connect("data/flights.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        tail TEXT,
        dep TEXT,
        arr TEXT,
        via TEXT,
        totaltime REAL,
        pic REAL,
        sic REAL,
        multi REAL,
        night REAL,
        solo REAL,
        xc REAL,
        approaches REAL,
        xcdist REAL,
        dayto REAL,
        daylndstop REAL,
        nightto REAL,
        nightlndstop REAL,
        alllandings REAL,
        hardimc REAL,
        hoodsim REAL,
        holds REAL,
        nvg REAL,
        nvgops REAL,
        dualgiven REAL,
        dualreceived REAL,
        simulated REAL,
        ground REAL,
        groundgiven REAL,
        signing TEXT
        )
    """)

    conn.commit()
    conn.close()

def insertFlight(entry):
    conn = sq.connect("data/flights.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO flights (
            date, tail, approaches, dep, arr, via, totaltime, pic, sic, multi, night,
            solo, xc, xcdist, dayto, daylndstop, nightto, nightlndstop, alllandings,
            hardimc, hoodsim, holds, nvg, nvgops, dualgiven, dualreceived, simulated,
            ground, groundgiven, signing
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry["date"], entry["tail"], entry["approaches"], entry["dep"], entry["arr"], entry["via"],
        entry["totaltime"], entry["pic"], entry["sic"], entry["multi"], entry["night"], entry["solo"],
        entry["xc"], entry["xcdist"], entry["dayto"], entry["daylndstop"], entry["nightto"],
        entry["nightlndstop"], entry["alllandings"], entry["hardimc"], entry["hoodsim"],
        entry["holds"], entry["nvg"], entry["nvgops"], entry["dualgiven"], entry["dualreceived"],
        entry["simulated"], entry["ground"], entry["groundgiven"], entry["signing"]
    ))

    conn.commit()
    conn.close()

def getAllFlights():
    conn = sq.connect("data/flights.db")
    df = pd.read_sql_query("SELECT * FROM flights ORDER BY date DESC", conn)
    conn.close()
    return df