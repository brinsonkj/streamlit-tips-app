{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKQNoZhja+Zmj3F9bJXP8z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/brinsonkj/streamlit-tips-app/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wMrIkzhYbIrX"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "\n",
        "df=pd.read_csv('Advertising_F.csv')\n",
        "st.title(\"Advertising Effectiveness Marlin\")\n",
        "st.sidebar.header(\"Filters\")\n",
        "x_var=st.sidebar.selectbox(\"X axis\",[\"TV\",\"radio\",\"newspaper\"])\n",
        "y_var=st.sidebar.selectbox(\"Y Axis\",[\"sales\"])\n",
        "\n",
        "#show scatterplot\n",
        "fig=px.scatter(df,x=x_var,y=y_var)\n",
        "st.plotly_chart(fig)\n",
        "\n",
        "#Dataframe\n",
        "st.write(\"### This is the data\")\n",
        "st.dataframe(df)\n",
        "\n",
        "#Show Map\n",
        "st.title(\"I'm the map!!!\")\n",
        "fig=px.scatter_mapbox(df,lat='latitude',lon='longitude',size='newspaper',\n",
        "                      hover_name='City',color='sales',\n",
        "                      color_continuous_scale=px.colors.sequential.Viridis)\n",
        "fig.update_layout(mapbox_style='carto-positron')\n",
        "st.plotly_chart(fig)"
      ]
    }
  ]
}