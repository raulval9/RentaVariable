{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMplM9eOSaRvzagoYJNe2PV",
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
        "<a href=\"https://colab.research.google.com/github/raulval9/RentaVariable/blob/main/ConsultaPrecios.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "f-fAHzS8cMie",
        "outputId": "4236991a-2897-4cb8-ecfe-52f5152914c8"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (ipython-input-2725983965.py, line 57)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipython-input-2725983965.py\"\u001b[0;36m, line \u001b[0;32m57\u001b[0m\n\u001b[0;31m    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "import yfinance as yf\n",
        "import pandas as pd\n",
        "\n",
        "# Configuración de la página\n",
        "st.set_page_config(page_title=\"Consulta de Precios y Volumen\", layout=\"centered\")\n",
        "st.title(\"📊 Consulta de precios históricos y volúmenes\")\n",
        "st.markdown(\"Consulta el precio de cierre y volumen negociado de cualquier acción, fondo, ETF o criptomoneda.\")\n",
        "\n",
        "# Input del usuario\n",
        "ticker = st.text_input(\"🔍 Ingresa el ticker (clave de pizarra):\", \"AAPL\")\n",
        "\n",
        "# Frecuencia\n",
        "frecuencia = st.selectbox(\"🕒 Frecuencia:\", [\"Diaria\", \"Semanal\", \"Mensual\"])\n",
        "intervalos = {\"Diaria\": \"1d\", \"Semanal\": \"1wk\", \"Mensual\": \"1mo\"}\n",
        "\n",
        "# Plazo\n",
        "plazo = st.selectbox(\"📅 Plazo:\", [\"1 día\", \"1 mes\", \"3 meses\", \"6 meses\", \"12 meses\", \"5 años\"])\n",
        "plazos = {\"1 día\": \"1d\", \"1 mes\": \"1mo\", \"3 meses\": \"3mo\", \"6 meses\": \"6mo\", \"12 meses\": \"1y\", \"5 años\": \"5y\"}\n",
        "\n",
        "# Botón para obtener datos\n",
        "if st.button(\"🔽 Obtener datos\"):\n",
        "    try:\n",
        "        data = yf.Ticker(ticker).history(period=plazos[plazo], interval=intervalos[frecuencia])\n",
        "        if data.empty:\n",
        "            st.warning(\"⚠️ No se encontraron datos para los criterios seleccionados.\")\n",
        "        else:\n",
        "            precios_volumen = data[['Close', 'Volume']].rename(columns={\n",
        "                'Close': 'Precio de Cierre',\n",
        "                'Volume': 'Volumen'\n",
        "            })\n",
        "\n",
        "            st.success(f\"✅ Datos obtenidos para {ticker}\")\n",
        "            st.subheader(\"📈 Precio de Cierre\")\n",
        "            st.line_chart(precios_volumen['Precio de Cierre'])\n",
        "\n",
        "            st.subheader(\"📊 Volumen Negociado\")\n",
        "            st.bar_chart(precios_volumen['Volumen'])\n",
        "\n",
        "            # Preparar Excel para descarga\n",
        "            precios_volumen.index = precios_volumen.index.tz_localize(None)\n",
        "            excel_file = f\"{ticker}_{intervalos[frecuencia]}_{plazos[plazo]}.xlsx\"\n",
        "            precios_volumen.to_excel(excel_file)\n",
        "\n",
        "            with open(excel_file, \"rb\") as f:\n",
        "                st.download_button(\n",
        "                    \"📥 Descargar Excel con precios y volumen\",\n",
        "                    f,\n",
        "                    file_name=excel_file,\n",
        "                    mime=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\"\n",
        "                )\n",
        "    except Exception as e:\n",
        "        st.error(f\"❌ Ocurrió un error: {e}\")\n",
        "\n",
        "!st run app.py\n",
        "streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "6PF-5AjSeYTz",
        "outputId": "4e77ad6c-586c-46c4-caca-59a401455147"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (ipython-input-1609277159.py, line 1)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipython-input-1609277159.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    streamlit run /usr/local/lib/python3.12/dist-packages/colab_kernel_launcher.py\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}