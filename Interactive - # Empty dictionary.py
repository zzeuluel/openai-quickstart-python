{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to Python 3.11.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ea7f988-1b08-4a22-b235-f56989df19cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "person = {\n",
    "    \"name\": \"Alice\",\n",
    "    \"age\": 30,\n",
    "    \"city\": \"New York\"\n",
    "}\n",
    "\n",
    "person\n",
    "\n",
    "# Different ways to create\n",
    "scores = dict(math=95, english=87, science=92)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa6863fc-41c6-41ad-8bff-a8ff7d139759",
   "metadata": {},
   "outputs": [],
   "source": [
    "from unicodedata import name\n",
    "\n",
    "\n",
    "person = {\n",
    "    \"name\": \"Alice\",\n",
    "    \"age\": 30,\n",
    "    \"city\": \"New York\"\n",
    "}\n",
    "\n",
    "person [\"name\"] = \"Dave\"\n",
    "\n",
    "person[\"licence\"] = True\n",
    "\n",
    "del person [\"licence\"]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
