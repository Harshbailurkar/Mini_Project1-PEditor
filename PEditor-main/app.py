# main app file
# contains frontend and backend logic
# streamlit is used as st
# pdfminer is used to perform all pdf related tasks


# importing liabraries
import streamlit as st
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF


# Use wide option to view full page
st.set_page_config(layout="wide")

# setting up app title
st.markdown(""" 
# PEditor
""")


# setting up menu  buttons
rad = st.sidebar.radio(" Menu", ["Home", "Help", "About us", "Contact us"])

# if else staements for switching from one option to another
if rad == "Home":

    # displaying an image and tagline
    st.markdown("""
    ## :outbox_tray: PDF Text Extractor: PDF to Text



    Before extracting information from a document, we have to extract text data first. 
    Hence, this PDF text data extractor was created.
    """)


# connecting download features to sidebar functions
    with st.sidebar:
        st.title("PDF to Text")
        textOutput = st.selectbox(
            "How do you want your output data?",
            ('One text file (.txt)', 'Text file per page (ZIP)'))

    pdf_file = st.file_uploader("Load your PDF file", type="pdf")

    if pdf_file:

        # display document
        with st.expander("Display document"):
            displayPDF(pdf_file)

        # pdf to text
        if textOutput == 'One text file (.txt)':
            text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
            totalPages = str(nbPages)+" pages in total."
            st.info(totalPages)
            st.download_button("Download txt file", text_data_f)

        # adding ballons animation
            st.balloons()

        else:
            text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
            totalPages = str(nbPages)+" pages in total."
            st.info(totalPages)
            zipPath = save_pages(text_data)

            # download text data
            with open(zipPath, "rb") as fp:
                btn = st.download_button(
                    label="Download ZIP (txt)",
                    data=fp,
                    file_name="pdf_to_txt.zip",
                    mime="application/zip"
                )

                # adding ballons animation
                st.balloons()


# help section
if rad == "Help":

    #  how to use section
    st.markdown("""
    ## How to use...
        """)

    st.markdown("""    
        1.To extract all text of pdf use One text file (.txt) option.
        """)

    st.markdown(""" 
        2.To extract a specific page or each pages text in a separate 
        page then select Text file per page (ZIP) option.
        """)

    st.markdown("""    
        3.To view pdf use Display document option.
    """)

    st.markdown("""    
        4.To edit and save pdf select threee dots option in right corner after using Display document option.
    """)


# note section
    st.markdown("""    
    ## Note:
    """)

    st.markdown(""" 
            1.Do not upload file size greater than 200mb.
            """)

    st.markdown(""" 
            2.Do not upload same file in a single session.To use the 
            same file or pdf refresh the app.
            """)

    st.markdown(""" 
            3.App supports only English language.
            """)

    st.markdown(""" 
            4.Do not use to extract a text data in a table,graph or in tabular format.It may didn't work properly.
            """)

    st.markdown(""" 
            5.Dosen't support to OCR.
            """)

    # st.write("Hiii")
    # st.write("This part is still in beta condition.......................👷‍♂️👷‍♂️👷")


# about us section
if rad == "About us":

    st.markdown("""
    #  Developed by.....
    """)

    st.markdown("""
    ## Our team
    """)

    st.write("Our team is located in  India , which developed our P2Extractor app.We have long been committed to providing simple and high-quality creative solutions, data solution software, PDF solutions  & tools. We have our own development team, aiming to provide software Design, Development, Maintenance and Update, as well as the software services. ")

    # settting two columns
    col1, col2 = st.columns(2)

    # creating 1st column
    col1.header("Mission")


# writing text to  column 1
    col1.write("We constantly develop and update the Internet products and services that are valuable to our clients.We take great pride in developing and providing multimedia and business software solutions to our clients.")


# creating 2nd column
    col2.header("Vision")

    # writing text to 2nd column
    col2.write("In the future, we strive to become the leading independent software and service provider.We are devoted to becoming an outstanding developer team to fulfill the needs of our users in better way. We will make our applications impact the digital lifestyle on users of all levels.")


# contact us section
if rad == "Contact us":

    # settting three  columns or two columns as per needs
    col1, col2, = st.columns(2)

    # creating 1st column
    col1.header("Technical Support")


# writing text to 1st column
    col1.write("If you need our technical & customer support, or have a question or problem, please visit our github profile given in follow us section.")

    # creating  2nd column
    col2.header("Business Inquiry")

    # writing text to 2nd column
    col2.write("Interested in reselling, distributing our products, and other partnership or business opportunities, please contact us through: harshbailurkar@gmail.com")

    # adding gmail icon to open gmail tab in browser
    col2.markdown("""
        [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
)](https://mail.google.com/mail/u/0/?ogbl#inbox)
""")

    # extra code of column 3 still in beta condition
    # column 3
    # col3.header("Promotions")
    # col3.write("If you wish to promote our product or software with a competition based giveaway, please email or use Skype to contact us through:")
