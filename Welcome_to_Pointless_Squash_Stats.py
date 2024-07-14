import streamlit as st


# App title
st.title("Welcome to \"Pointless Squash Stats\"!")
st.write("Where squash isn't just a vegetable.")

# Intro content
st.write("""
In the realm of squash, where every swing, smash, and slide counts, it's often the banter that lingers longer than the actual scores. 
But why rely solely on memory and wit? Memories fade, your digital footprints won't. Back your pre- and postgame trashtalk with serious, objective performance statistics.
""")

# Section 1
st.subheader("1. Racquet Records: Document your match results")
st.write("""
Document each exhilarating (or ego-crushing) match result.
Each match you play, every score you chalk up, is more than just a number — it's a testament to skill, strategy, and that sneaky drop shot you've been perfecting. 
Whether it's an earth-shattering victory or a humble hiccup, it'll be archived here in all its glory.
""")
if st.button("Jump to the pointless racquet records"):
    st.switch_page("pages/1_Pointless_Racquet_Records.py")

# Section 2
st.subheader("2. Overanalysis Oasis: Delving Deep into Data Details.")
st.write("""
Data has a story to tell, and boy, do we love to narrate! 
From the trajectory of your winning streaks to the pattern of your losses, we dissect every detail. 
Want to know how often you've beaten Chris on a Wednesday evening? Or which month you truly peaked? 
We're on it, with charts, graphs, and narratives that are almost obsessively granular.
""")
if st.button("Dive into the pointless overanalysis oasis"):
    st.switch_page("pages/2_Pointless_Overanalysis_Oasis.py")


# Footer
st.write("""
Step into "Pointless Squash Stats", where numbers narrate the nonsense and amusement is always ace.
""")
st.write("👈 Explore by clicking on the chevron on the top of your screen to unfold the sidebar!")
