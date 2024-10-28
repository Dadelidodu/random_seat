import streamlit as st
import io
import pandas as pd
from openspace import Openspace

def main():

    # Set up the Streamlit interface
    st.title("Bouman_8 Turning Tables !")

    # Table and seat settings
    set_tables = st.number_input('Set the number of tables in the openspace', min_value=1, step=1)
    set_seats = st.number_input('Set the number of seats per table in the openspace', min_value=1, step=1)

    # File upload widget
    uploaded_file = st.file_uploader("Upload your xlsx file with names", type="xlsx")

    # Variable to track arrangement
    arrangement_df = None

    if uploaded_file and set_tables and set_seats:
        # Load the uploaded Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)
        if "Names" in df.columns:
            file_path = df["Names"].tolist()
            
            # Create an Openspace instance and organize seating
            op = Openspace(set_tables, set_seats)
            
            # Check if 'Rescramble' button is clicked to reshuffle
            if st.button("Rescramble") or arrangement_df is None:
                op.organize(file_path)
            
            # Get the seating arrangement DataFrame from the Openspace instance
            arrangement_df = op.display()  # Get the DataFrame directly

            # Display organized seating arrangement
            st.subheader("Seating Arrangement")
            if not arrangement_df.empty:
                st.dataframe(arrangement_df)

            # Save organized arrangement to a file
            output = io.StringIO()
            arrangement_df.to_csv(output, index=False)
            output.seek(0)

            # Add a download button for the CSV
            st.download_button(
                label="Download Arrangement as CSV",
                data=output.getvalue(),
                file_name='Random_distribution_output.csv',
                mime='text/csv'
            )    
        else:
            st.error("The uploaded file must contain a 'Names' column.")
    else:
        st.info("Please upload a file and specify the number of tables and seats.")

main()

# streamlit run C:\Users\Hello\Desktop\app_deploy\randomseat_app.py