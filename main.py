import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Parental Involvement Pie Chart with Live Input ---
st.title('Parental Involvement and Satisfaction Levels')

# Live input for respondents in each category
highly_involved = st.slider('Number of Highly Involved Respondents', 0, 50, 18)
moderately_involved = st.slider('Number of Moderately Involved Respondents', 0, 50, 22)
not_involved = st.slider('Number of Not Involved Respondents', 0, 50, 10)

# Satisfaction Scores can be adjusted as well
highly_involved_satisfaction = st.slider('Satisfaction Score for Highly Involved', 1.0, 5.0, 4.5, 0.1)
moderately_involved_satisfaction = st.slider('Satisfaction Score for Moderately Involved', 1.0, 5.0, 3.9, 0.1)
not_involved_satisfaction = st.slider('Satisfaction Score for Not Involved', 1.0, 5.0, 3.2, 0.1)

# Data for Pie chart
labels = ['Highly Involved', 'Moderately Involved', 'Not Involved']
sizes = [highly_involved, moderately_involved, not_involved]
satisfaction_scores = [highly_involved_satisfaction, moderately_involved_satisfaction, not_involved_satisfaction]

# Creating Pie chart with shadow effect
fig1, ax1 = plt.subplots(figsize=(7, 7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'], shadow=True)
ax1.set_title('Parental Involvement and Satisfaction Levels')
ax1.axis('equal')

# Display Pie chart
st.pyplot(fig1)

# --- 3D Bar Chart for Satisfaction Level by School Type ---
st.title('Satisfaction Level by Type of School')

# Live input for school types and satisfaction scores
school_types = ['Private', 'Public']
private_satisfaction = st.slider('Satisfaction Score for Private School', 1.0, 5.0, 4.3, 0.1)
public_satisfaction = st.slider('Satisfaction Score for Public School', 1.0, 5.0, 3.7, 0.1)

# Create 3D figure
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# X-axis positions
x_pos = np.arange(len(school_types))

# Create bars
ax2.bar(x_pos, [private_satisfaction, public_satisfaction], zdir='y', color=['blue', 'green'])

# Labeling the axes
ax2.set_xlabel('School Type')
ax2.set_ylabel('Category')
ax2.set_zlabel('Satisfaction Score')

# Set tick labels
ax2.set_xticks(x_pos)
ax2.set_xticklabels(school_types)

# Set Title
ax2.set_title('3D Satisfaction Level by Type of School')

# Display 3D Bar chart
st.pyplot(fig2)
