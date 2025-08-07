import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")

genai.configure(api_key=gemini_api_key)

class WaterQualityAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def analyze_water_data(self, water_data):
        """
        Analyze water quality data and provide recommendations
        """
        prompt = self._create_analysis_prompt(water_data)

        try:
            response = self.model.generate_content(prompt)
            return self._parse_response(response.text)
        except Exception as e:
            return {
                "error": f"Failed to analyze water data: {str(e)}",
                "recommendations": [],
                "quality_assessment": "Unable to assess",
                "risk_level": "Unknown"
            }

    def _create_analysis_prompt(self, data):
        """
        Create a detailed prompt for water quality analysis
        """
        prompt = f"""
        You are a water quality expert specializing in SDG 6 (Clean Water and Sanitation). 
        Analyze(considering the WHO standard values) the following water quality data and provide actionable recommendations:

        WATER QUALITY DATA:
        - Location: {data.get('location', 'Not specified')}
        - Water Source: {data.get('water_source', 'Not specified')}
        - pH Level: {data.get('ph_level', 'Not specified')}
        - Turbidity (NTU): {data.get('turbidity', 'Not specified')}
        - Total Dissolved Solids (mg/L): {data.get('tds', 'Not specified')}
        - Free Chlorine (mg/L): {data.get('chlorine', 'Not specified')}
        - E. coli Count (CFU/100mL): {data.get('bacteria_count', 'Not specified')}
        - Nitrates (mg/L): {data.get('nitrates', 'Not specified')}
        - Fluoride (mg/L): {data.get('fluoride', 'Not specified')}
        - Iron (mg/L): {data.get('iron', 'Not specified')}
        - Water Hardness (mg/L as CaCO3): {data.get('hardness', 'Not specified')}
        - Additional Observations: {data.get('additional_notes', 'None')}

        Please provide your analysis in the following JSON format:
        {{
            "quality_assessment": "Overall water quality status (Excellent/Good/Fair/Poor/Critical)",
            "risk_level": "Health risk level (Low/Medium/High/Critical)",
            "key_issues": ["List of main water quality issues identified"],
            "immediate_actions": ["Urgent actions needed within 1-7 days"],
            "short_term_solutions": ["Solutions implementable within 1-6 months"],
            "long_term_solutions": ["Sustainable solutions for 6+ months"],
            "cost_estimates": {{
                "immediate": "Estimated cost for immediate actions",
                "short_term": "Estimated cost for short-term solutions",
                "long_term": "Estimated cost for long-term solutions"
            }},
            "health_impacts": ["Potential health impacts if issues are not addressed"],
            "sdg6_alignment": "How these recommendations align with SDG 6 targets",
            "monitoring_plan": ["Parameters to monitor regularly"],
            "community_involvement": ["Ways the local community can participate"]
        }}

        Focus on practical, cost-effective solutions that can be implemented in the specified location.
        Consider local resources, climate, and socioeconomic factors.
        """
        return prompt

    def _parse_response(self, response_text):
        """
        Parse the AI response and extract structured data
        """
        try:
            # Try to extract JSON from the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1

            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                return json.loads(json_str)
            else:
                # If no JSON found, return a structured response with the raw text
                return {
                    "quality_assessment": "Analysis completed",
                    "risk_level": "See full analysis",
                    "key_issues": ["See detailed analysis below"],
                    "recommendations": response_text,
                    "full_analysis": response_text
                }
        except json.JSONDecodeError:
            # If JSON parsing fails, return the raw response
            return {
                "quality_assessment": "Analysis completed",
                "risk_level": "See full analysis",
                "recommendations": response_text,
                "full_analysis": response_text
            }

# Initialize the analyzer
analyzer = WaterQualityAnalyzer()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_water():
    """API endpoint to analyze water quality data"""
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        required_fields = ['location', 'water_source', 'ph_level', 'turbidity']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400
        
        # Analyze the water data
        analysis_result = analyzer.analyze_water_data(data)
        
        return jsonify({
            "status": "success",
            "analysis": analysis_result
        })
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Water Quality AI Analyzer",
        "sdg": "SDG 6 - Clean Water and Sanitation"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
