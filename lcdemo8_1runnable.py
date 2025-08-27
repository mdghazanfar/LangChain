from langchain.schema.runnable import Runnable
from typing import Dict, List, Generator, Any, Optional, Union
import streamlit as st
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SportsRunnable(Runnable):
    """
    A Runnable interface implementation for sports information processing.
    Handles queries about popular sports in different countries.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the SportsRunnable with configuration and sports data.
        
        Args:
            config (Optional[Dict[str, Any]]): Configuration parameters
        """
        self.config = {
            "max_tokens": 50,
            "temperature": 0.7,
            **(config or {})
        }
        
        # Expanded sports data dictionary
        self.sports_data = {
            "USA": {
                "sports": ["Basketball", "American Football", "Baseball"],
                "national_sport": "Baseball",
                "popular_leagues": ["NBA", "NFL", "MLB"]
            },
            "India": {
                "sports": ["Cricket", "Hockey", "Football"],
                "national_sport": "Hockey",
                "popular_leagues": ["IPL", "ISL", "Hockey India League"]
            },
            "Brazil": {
                "sports": ["Football", "Volleyball", "Formula 1"],
                "national_sport": "Football",
                "popular_leagues": ["Brasileirão", "Superliga", "Stock Car Brasil"]
            }
        }
        
        logger.info("SportsRunnable initialized successfully")

    def _validate_input(self, country: str) -> tuple[bool, str]:
        """
        Validate the input country name.
        
        Args:
            country (str): Country name to validate
            
        Returns:
            tuple[bool, str]: Validation result and message
        """
        if not country:
            return False, "Please provide a country name."
        if country not in self.sports_data:
            return False, f"No sports data available for {country}. Please try another country."
        return True, ""

    def invoke(self, input: Dict[str, str], config: Optional[Dict[str, Any]] = None) -> str:
        """
        Process a single input request.
        
        Args:
            input (Dict[str, str]): Input dictionary containing country name
            config (Optional[Dict[str, Any]]): Optional configuration override
            
        Returns:
            str: Formatted response with sports information
        """
        try:
            country = input.get("country", "").strip()
            is_valid, message = self._validate_input(country)
            
            if not is_valid:
                return message
            
            country_data = self.sports_data[country]
            sports_list = ", ".join(country_data["sports"])
            
            response = (
                f"Popular sports in {country}:\n"
                f"• Main sports: {sports_list}\n"
                f"• National sport: {country_data['national_sport']}\n"
                f"• Popular leagues: {', '.join(country_data['popular_leagues'])}"
            )
            
            logger.info(f"Successfully processed request for country: {country}")
            return response
            
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return f"Error processing request: {str(e)}"

def main():
    """Main Streamlit application"""
    try:
        st.set_page_config(
            page_title="Sports Arena",
            page_icon="🏆",
            layout="wide"
        )
        
        st.title("🏆 Sports-Arena")
        st.subheader("Discover Popular Sports by Country")
        
        # Add context in a nice format
        with st.expander("ℹ️ About this app", expanded=True):
            st.markdown("""
            This app provides information about popular sports in different countries.
            Currently supported countries:
            - 🇺🇸 USA
            - 🇮🇳 India
            - 🇧🇷 Brazil
            """)
        
        # Create two columns for input and results
        col1, col2 = st.columns([1, 2])
        
        with col1:
            country = st.text_input(
                "Enter your country:",
                placeholder="e.g., USA",
                key="country_input"
            )
        
        if country:
            try:
                runnable = SportsRunnable()
                with st.spinner('🔍 Fetching sports information...'):
                    response = runnable.invoke({"country": country})
                
                with col2:
                    st.success(response)
                    
                    # Add timestamp for last updated
                    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            except Exception as e:
                logger.error(f"Application error: {str(e)}")
                st.error(f"An error occurred: {str(e)}")
        
        # Add footer with additional information
        st.markdown("---")
        st.markdown(
            """
            <div style='text-align: center'>
                Built with ❤️ using Langchain and Streamlit
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        logger.error(f"Fatal application error: {str(e)}")
        st.error("A fatal error occurred. Please try again later.")

if __name__ == "__main__":
    main()
