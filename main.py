import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Pie Chart for Satisfaction Level by Parental Involvement ---
st.title('Parental Involvement and Satisfaction Levels')

# Data for Satisfaction Level by Parental Involvement
labels = ['Highly Involved', 'Moderately Involved', 'Not Involved']
sizes = [18, 22, 10]  # Number of respondents in each category
satisfaction_scores = [4.5, 3.9, 3.2]  # Average satisfaction scores

# Creating Pie chart with shadow effect for 3D-like appearance
fig1, ax1 = plt.subplots(figsize=(7, 7))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'], shadow=True)
ax1.set_title('Parental Involvement and Satisfaction Levels')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display Pie chart
st.pyplot(fig1)

# --- 3D Bar Chart for Satisfaction Level by School Type ---
st.title('Satisfaction Level by Type of School')

# Data for Satisfaction Level by School Type
school_types = ['Private', 'Public']
satisfaction_scores = [4.3, 3.7]

# Create 3D figure
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# X-axis positions
x_pos = np.arange(len(school_types))

# Create bars
ax2.bar(x_pos, satisfaction_scores, zdir='y', color=['blue', 'green'])

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
