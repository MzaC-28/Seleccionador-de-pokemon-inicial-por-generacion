{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPQOJdAv7mC/GhcLU4w69vU",
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
        "<a href=\"https://colab.research.google.com/github/MzaC-28/Seleccionador-de-pokemon-inicial-por-generacion/blob/main/Andy_Meza_Funciones.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vXUT7-CRYmDu",
        "outputId": "3b6b5de6-d700-4808-8bb0-e87c7231e96b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. Sumar\n",
            "2. Restar\n",
            "3. Multiplicar\n",
            "4. Dividir\n",
            "5. Potencia\n",
            "6. Salir\n",
            "Ingrese una opción del menu: 5\n",
            "Ingrese el primer número: 8\n",
            "Ingrese el segundo número: 2\n",
            "64.0\n",
            "None\n"
          ]
        }
      ],
      "source": [
        "def mostrar_menu():\n",
        "  print(\"1. Sumar\")\n",
        "  print(\"2. Restar\")\n",
        "  print(\"3. Multiplicar\")\n",
        "  print(\"4. Dividir\")\n",
        "  print(\"5. Potencia\")\n",
        "  print(\"6. Salir\")\n",
        "\n",
        "def sumar():\n",
        "  numero1 = float(input(\"Ingrese el primer número: \"))\n",
        "  numero2 = float(input(\"Ingrese el segundo número: \"))\n",
        "  resultado = numero1 + numero2\n",
        "  return resultado\n",
        "\n",
        "def restar():\n",
        "  numero1 = float(input(\"Ingrese el primer número: \"))\n",
        "  numero2 = float(input(\"Ingrese el segundo número: \"))\n",
        "  resultado = numero1 - numero2\n",
        "  return resultado\n",
        "\n",
        "def multiplicar():\n",
        "  numero1 = float(input(\"Ingrese el primer número: \"))\n",
        "  numero2 = float(input(\"Ingrese el segundo número: \"))\n",
        "  resultado = numero1 * numero2\n",
        "  return resultado\n",
        "\n",
        "def dividir():\n",
        "  numero1 = float(input(\"Ingrese el primer número: \"))\n",
        "  numero2 = float(input(\"Ingrese el segundo número: \"))\n",
        "  if numero2 != 0:\n",
        "    resultado = numero1 / numero2\n",
        "    return resultado\n",
        "  else:\n",
        "    print(\"No se puede dividir para 0\")\n",
        "\n",
        "def potencia():\n",
        "  numero1 = float(input(\"Ingrese el primer número: \"))\n",
        "  numero2 = float(input(\"Ingrese el segundo número: \"))\n",
        "  resultado = numero1 ** numero2\n",
        "  return resultado\n",
        "\n",
        "def salir():\n",
        "  print(\"Gracias por usar el sistema\")\n",
        "\n",
        "def eleccion():\n",
        "  mostrar_menu()\n",
        "\n",
        "  opcion = input(\"Ingrese una opción del menu: \")\n",
        "  if opcion == \"1\":\n",
        "    resultado = sumar()\n",
        "    print(resultado)\n",
        "  elif opcion == \"2\":\n",
        "    resultado = restar()\n",
        "    print(resultado)\n",
        "  elif opcion == \"3\":\n",
        "    resultado = multiplicar()\n",
        "    print(resultado)\n",
        "  elif opcion == \"4\":\n",
        "    resultado = dividir()\n",
        "    print(resultado)\n",
        "  elif opcion == \"5\":\n",
        "    resultado = potencia()\n",
        "    print(resultado)\n",
        "  elif opcion == \"6\":\n",
        "    salir()\n",
        "  else:\n",
        "    print(\"Opción no disponible\")\n",
        "\n",
        "eleccion = eleccion()\n",
        "print(eleccion)"
      ]
    }
  ]
}