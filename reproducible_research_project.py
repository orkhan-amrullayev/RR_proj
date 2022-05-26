{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Churn Rate\n",
    "\n",
    "## Project Overview\n",
    "\n",
    "This project made to obtain grades for Reproducible Research class at the University of Warsaw.  \n",
    "\n",
    "Our group:\n",
    "1. Orkhan Amrullayev\n",
    "2. Srinesh Heshan\n",
    "3. Laura Florencia\n",
    "\n",
    "The project's aim to predict behaviour of teleco customer. The dataset itself comes from kaggle (URL at the reference). Here we would like to analyze from the customer's data then see the churn implies to retention approach based on one base paper and we do the improvement. \n",
    "\n",
    "We will predict how the customer will churn by analyze the details:  \n",
    "* Account information\n",
    "* Demographic information\n",
    "* Services information  \n",
    "\n",
    "By those parameters, we will also know how to increase the customer satisfaction and somehow improve the previous research. We are now using Tensorflow library as the differenciate and some algorithms to get the different result."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Weka Data Mining Tool\n",
    "\n",
    "Here they have used weka which is a data mining tool for small scale projects. \n",
    "\n",
    "Weka features include machine learning, data mining, preprocessing, classification, regression, clustering, association rules, attribute selection, experiments, workflow and visualization. Weka is written in Java, developed at the University of Waikato, New Zealand."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Google Colab\n",
    "\n",
    "Why do we using Colab?\n",
    "\n",
    "Colaboratory, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education.\n",
    "\n",
    "\n",
    "Notebooks can stay connected for up to 24 hours, compared to the 12 hours in the free version of Colab notebooks. Get priority access to high-memory VMs. These VMs generally have double the memory of standard Colab VMs and twice as many CPUs. Users might even be automatically given a high-memory VM when Colab detects that the need. Another feature is absent in the free version. To offer faster GPUs, longer runtimes and more memory in Colab for a relatively low price, Google needs to maintain the flexibility to adjust usage limits and the availability of hardware on the fly. \n",
    "\n",
    "Resources in Colab Pro are prioritised for subscribers who have recently used fewer resources, in order to prevent the monopolisation of limited resources by a small number of users. To get the most out of Colab Pro, consider closing your Colab tabs when you are done with your work, and avoid opting for GPUs or extra memory when it is not needed for your work. \n",
    "This will make it less likely for a user to run into usage limits within Colab Pro."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Dataset Detail  \n",
    "\n",
    "Dataset contains 7043 rows and 34 columns. The rows comes from customers data and the column represent the features in dataset. However, we will just drop some columns, and will only use 19 independet variables and 1 dependent variables.\n",
    "\n",
    "Target variable/ dependent variable: column \"churn value\" (we also have \"churn label\" in the column, but we will use the \"churn value\" as it is easy to use - integer value).  \n",
    "\n",
    "Independent variables: 19 columns which represent the characteristics of customers.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Load libraries\n",
    "\n",
    "Libraries that we are using to reproducible the research."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "'C:\\Users\\Laura' is not recognized as an internal or external command,\n",
      "operable program or batch file.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:07.613592Z",
     "iopub.status.busy": "2022-05-25T19:11:07.613201Z",
     "iopub.status.idle": "2022-05-25T19:11:07.625825Z",
     "shell.execute_reply": "2022-05-25T19:11:07.624363Z",
     "shell.execute_reply.started": "2022-05-25T19:11:07.613550Z"
    }
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-fd8c78e71dca>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mseaborn\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0msns\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mtensorflow\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mtf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mutil\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtesting\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mtm\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import tensorflow as tf\n",
    "import pandas.util.testing as tm\n",
    "\n",
    "from xgboost import XGBClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler, RobustScaler, LabelEncoder\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "from sklearn.utils import resample\n",
    "\n",
    "%matplotlib inline\n",
    "pd.options.display.max_columns = 500\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Load data\n",
    "\n",
    "Load the dataset that we are using as the source of the research."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:08.044077Z",
     "iopub.status.busy": "2022-05-25T19:11:08.043279Z",
     "iopub.status.idle": "2022-05-25T19:11:08.090219Z",
     "shell.execute_reply": "2022-05-25T19:11:08.089256Z",
     "shell.execute_reply.started": "2022-05-25T19:11:08.044026Z"
    }
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('Churn_dataset.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis (EDA)\n",
    "\n",
    "We are showing the small detail of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:08.495608Z",
     "iopub.status.busy": "2022-05-25T19:11:08.495199Z",
     "iopub.status.idle": "2022-05-25T19:11:08.525304Z",
     "shell.execute_reply": "2022-05-25T19:11:08.523885Z",
     "shell.execute_reply.started": "2022-05-25T19:11:08.495574Z"
    }
   },
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:08.939814Z",
     "iopub.status.busy": "2022-05-25T19:11:08.939372Z",
     "iopub.status.idle": "2022-05-25T19:11:08.972640Z",
     "shell.execute_reply": "2022-05-25T19:11:08.971072Z",
     "shell.execute_reply.started": "2022-05-25T19:11:08.939776Z"
    }
   },
   "outputs": [],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Apparently we have no null values, however TotalCharges has incorrect format (object), fix this converting it to float (float64) and filling missing values those will be generated during conversion with 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:09.536216Z",
     "iopub.status.busy": "2022-05-25T19:11:09.535609Z",
     "iopub.status.idle": "2022-05-25T19:11:09.551630Z",
     "shell.execute_reply": "2022-05-25T19:11:09.550495Z",
     "shell.execute_reply.started": "2022-05-25T19:11:09.536157Z"
    }
   },
   "outputs": [],
   "source": [
    "df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')\n",
    "df['TotalCharges'] = df['TotalCharges'].fillna(value=0)\n",
    "\n",
    "df['tenure'] = df['tenure'].astype('float64')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Drop customer ID as it's not relevant field for analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:09.951823Z",
     "iopub.status.busy": "2022-05-25T19:11:09.951116Z",
     "iopub.status.idle": "2022-05-25T19:11:09.960161Z",
     "shell.execute_reply": "2022-05-25T19:11:09.959035Z",
     "shell.execute_reply.started": "2022-05-25T19:11:09.951781Z"
    }
   },
   "outputs": [],
   "source": [
    "df.drop('customerID', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Splitting categorical and numerical columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:10.378820Z",
     "iopub.status.busy": "2022-05-25T19:11:10.378057Z",
     "iopub.status.idle": "2022-05-25T19:11:10.391199Z",
     "shell.execute_reply": "2022-05-25T19:11:10.390228Z",
     "shell.execute_reply.started": "2022-05-25T19:11:10.378779Z"
    }
   },
   "outputs": [],
   "source": [
    "col_cat = df.select_dtypes(include='object').drop('Churn', axis=1).columns.tolist()\n",
    "col_num = df.select_dtypes(exclude='object').columns.tolist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Analysis in Categorical Fields"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For our categorical fields, check how many unique values has each column so we will decide if feature engineering (and merging values in case there is too many of them) is needed.\n",
    "You will see we have 2-4 unique values that is ideal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:11.083431Z",
     "iopub.status.busy": "2022-05-25T19:11:11.082652Z",
     "iopub.status.idle": "2022-05-25T19:11:11.105179Z",
     "shell.execute_reply": "2022-05-25T19:11:11.104179Z",
     "shell.execute_reply.started": "2022-05-25T19:11:11.083390Z"
    }
   },
   "outputs": [],
   "source": [
    "for c in col_cat:\n",
    "    print('Column {} unique values: {}'.format(c, len(df[c].unique())))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's look at the distribution of Churn by all categorical variables. We can see that gender is not correlated with Churn at all, but Contract is highly correlated with churn and customers with contract of month-to-month are more likely to churn than the customers with 1-year and 2-years contracts. It may lead company to promote 1 & 2 years contract.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:12.162929Z",
     "iopub.status.busy": "2022-05-25T19:11:12.162064Z",
     "iopub.status.idle": "2022-05-25T19:11:14.771182Z",
     "shell.execute_reply": "2022-05-25T19:11:14.770117Z",
     "shell.execute_reply.started": "2022-05-25T19:11:12.162881Z"
    }
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(20,20))\n",
    "for i,c in enumerate(col_cat):\n",
    "    plt.subplot(5,4,i+1)\n",
    "    sns.countplot(df[c], hue=df['Churn'])\n",
    "    plt.title(c)\n",
    "    plt.xlabel('')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here we have distribution of our numerical features\n",
    "It seems tenure is correlated with Churn.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:14.773572Z",
     "iopub.status.busy": "2022-05-25T19:11:14.773232Z",
     "iopub.status.idle": "2022-05-25T19:11:15.364614Z",
     "shell.execute_reply": "2022-05-25T19:11:15.363521Z",
     "shell.execute_reply.started": "2022-05-25T19:11:14.773539Z"
    }
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(20,5))\n",
    "for i,c in enumerate(['tenure', 'MonthlyCharges', 'TotalCharges']):\n",
    "    plt.subplot(1,3,i+1)\n",
    "    sns.distplot(df[df['Churn'] == 'No'][c], kde=True, color='blue', hist=False, kde_kws=dict(linewidth=2), label='No')\n",
    "    sns.distplot(df[df['Churn'] == 'Yes'][c], kde=True, color='Orange', hist=False, kde_kws=dict(linewidth=2), label='Yes')\n",
    "    plt.title(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Violin plot\n",
    "\n",
    "A violin plot is a hybrid of a box plot and a kernel density plot, *which shows peaks in the data*. It is used to visualize the distribution of numerical data of our variable which we prepared before. Unlike a box plot that can only show summary statistics, violin plots depict summary statistics and the density of each variable.  \n",
    "\n",
    "This violin plot shows the relationship of feed type to chick weight. The box plot elements show the median weight for horsebean-fed chicks is lower than for other feed types. The shape of the distribution (extremely skinny on each end and wide in the middle) indicates the weights of sunflower-fed chicks are highly concentrated around the median.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:15.366733Z",
     "iopub.status.busy": "2022-05-25T19:11:15.366370Z",
     "iopub.status.idle": "2022-05-25T19:11:15.998015Z",
     "shell.execute_reply": "2022-05-25T19:11:15.997017Z",
     "shell.execute_reply.started": "2022-05-25T19:11:15.366697Z"
    }
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(20,5))\n",
    "for i,c in enumerate(col_num):\n",
    "    plt.subplot(1,4,i+1)\n",
    "    sns.violinplot(x=df['Churn'], y=df[c])\n",
    "    plt.title(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data preprocessing\n",
    "\n",
    "After EDA, let's prepare our date for the machine learning algorithms. One hot encoding of our categorical features. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:16.000472Z",
     "iopub.status.busy": "2022-05-25T19:11:16.000151Z",
     "iopub.status.idle": "2022-05-25T19:11:16.030615Z",
     "shell.execute_reply": "2022-05-25T19:11:16.029415Z",
     "shell.execute_reply.started": "2022-05-25T19:11:16.000440Z"
    }
   },
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:16.046413Z",
     "iopub.status.busy": "2022-05-25T19:11:16.045885Z",
     "iopub.status.idle": "2022-05-25T19:11:16.109714Z",
     "shell.execute_reply": "2022-05-25T19:11:16.108894Z",
     "shell.execute_reply.started": "2022-05-25T19:11:16.046378Z"
    }
   },
   "outputs": [],
   "source": [
    "dfT = pd.get_dummies(df, columns=col_cat)\n",
    "dfT.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now do simple label encoding of our target variable Churn."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:16.570134Z",
     "iopub.status.busy": "2022-05-25T19:11:16.569562Z",
     "iopub.status.idle": "2022-05-25T19:11:16.581978Z",
     "shell.execute_reply": "2022-05-25T19:11:16.581067Z",
     "shell.execute_reply.started": "2022-05-25T19:11:16.570100Z"
    }
   },
   "outputs": [],
   "source": [
    "dfT['Churn'] = dfT['Churn'].map(lambda x: 1 if x == 'Yes' else 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Balanced or Imbalanced?\n",
    "\n",
    "Let's see if our dataset is balanced or imbalanced and if any action is needed. You will find out that data are highly imbalanced with ratio 2:5, so then we will use resample function to upsample the minority group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:17.473600Z",
     "iopub.status.busy": "2022-05-25T19:11:17.473010Z",
     "iopub.status.idle": "2022-05-25T19:11:17.602272Z",
     "shell.execute_reply": "2022-05-25T19:11:17.601436Z",
     "shell.execute_reply.started": "2022-05-25T19:11:17.473563Z"
    }
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(5, 5))\n",
    "sns.countplot(dfT['Churn'])\n",
    "plt.title('Imbalanced dataset, it seems ratio is 2:5 for Yes:No')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's divide our data into 2 groups, majority (0) and minority (1) and create new dataset by upsampling minority group."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:20.150004Z",
     "iopub.status.busy": "2022-05-25T19:11:20.149504Z",
     "iopub.status.idle": "2022-05-25T19:11:20.172634Z",
     "shell.execute_reply": "2022-05-25T19:11:20.171442Z",
     "shell.execute_reply.started": "2022-05-25T19:11:20.149964Z"
    }
   },
   "outputs": [],
   "source": [
    "minority = dfT[dfT.Churn==1]\n",
    "majority = dfT[dfT.Churn==0]\n",
    "\n",
    "minority_upsample = resample(minority, replace=True, n_samples=majority.shape[0])\n",
    "dfT = pd.concat([minority_upsample, majority], axis=0)\n",
    "dfT = dfT.sample(frac=1).reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's just have a quick check how it looked like before balance and after balance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:20.877696Z",
     "iopub.status.busy": "2022-05-25T19:11:20.877293Z",
     "iopub.status.idle": "2022-05-25T19:11:21.109524Z",
     "shell.execute_reply": "2022-05-25T19:11:21.108438Z",
     "shell.execute_reply.started": "2022-05-25T19:11:20.877663Z"
    }
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10, 5))\n",
    "plt.subplot(1,2,1)\n",
    "sns.countplot(df['Churn'])\n",
    "plt.title('Imbalanced dataset')\n",
    "\n",
    "plt.subplot(1,2,2)\n",
    "sns.countplot(dfT['Churn'])\n",
    "plt.title('Balanced dataset')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Time to Scale!\n",
    "\n",
    "Machine Learning algorithms are sensitive on data that are not normalized to same scale. We will use robust scaler which can nicely handle outliers, but standard scaler might work well too. This Scaler removes the median and scales the data according to the quantile range (defaults to IQR: Interquartile Range)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:11:21.973488Z",
     "iopub.status.busy": "2022-05-25T19:11:21.973118Z",
     "iopub.status.idle": "2022-05-25T19:11:21.989696Z",
     "shell.execute_reply": "2022-05-25T19:11:21.988363Z",
     "shell.execute_reply.started": "2022-05-25T19:11:21.973458Z"
    }
   },
   "outputs": [],
   "source": [
    "rs = RobustScaler()\n",
    "dfT['tenure'] = rs.fit_transform(dfT['tenure'].values.reshape(-1,1))\n",
    "dfT['MonthlyCharges'] = rs.fit_transform(dfT['MonthlyCharges'].values.reshape(-1,1))\n",
    "dfT['TotalCharges'] = rs.fit_transform(dfT['TotalCharges'].values.reshape(-1,1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Split\n",
    "\n",
    "Split our data into train & test partitions. Train partition will be used to train ML model, test will be used to validate it's performance. *70% goes to train, 30% goes to test*. It could be also 80:20 or 60:40, but we choose 70:30 in our research."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:40:18.719934Z",
     "iopub.status.busy": "2022-05-25T19:40:18.718221Z",
     "iopub.status.idle": "2022-05-25T19:40:18.756862Z",
     "shell.execute_reply": "2022-05-25T19:40:18.755404Z",
     "shell.execute_reply.started": "2022-05-25T19:40:18.719830Z"
    }
   },
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(dfT.drop('Churn', axis=1).values, dfT['Churn'].values, test_size=0.3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Modeling\n",
    "\n",
    "We will use Logistic Classifier, Decision Tree, Random Forest, XGBoost, Neural Network\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Logistic Regression\n",
    "\n",
    "Logistic regression is a process of modeling the probability of a discrete outcome given an input variable. The most common logistic regression models a binary outcome; something that can take two values such as true/false, yes/no, and so on.  The technique can also be used in engineering, especially for predicting the probability of failure of a given process, system or product. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:32.926576Z",
     "iopub.status.busy": "2022-05-25T19:41:32.926067Z",
     "iopub.status.idle": "2022-05-25T19:41:32.933160Z",
     "shell.execute_reply": "2022-05-25T19:41:32.931785Z",
     "shell.execute_reply.started": "2022-05-25T19:41:32.926536Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:33.918082Z",
     "iopub.status.busy": "2022-05-25T19:41:33.917613Z",
     "iopub.status.idle": "2022-05-25T19:41:33.924233Z",
     "shell.execute_reply": "2022-05-25T19:41:33.922853Z",
     "shell.execute_reply.started": "2022-05-25T19:41:33.918044Z"
    }
   },
   "outputs": [],
   "source": [
    "model_lg = LogisticRegression(max_iter=500,random_state=0, n_jobs=-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:34.591940Z",
     "iopub.status.busy": "2022-05-25T19:41:34.591272Z",
     "iopub.status.idle": "2022-05-25T19:41:35.831471Z",
     "shell.execute_reply": "2022-05-25T19:41:35.830153Z",
     "shell.execute_reply.started": "2022-05-25T19:41:34.591900Z"
    }
   },
   "outputs": [],
   "source": [
    "model_lg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:35.834845Z",
     "iopub.status.busy": "2022-05-25T19:41:35.834160Z",
     "iopub.status.idle": "2022-05-25T19:41:35.842283Z",
     "shell.execute_reply": "2022-05-25T19:41:35.841135Z",
     "shell.execute_reply.started": "2022-05-25T19:41:35.834784Z"
    }
   },
   "outputs": [],
   "source": [
    "# Making Predictions\n",
    "pred_lg = model_lg.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:37.483212Z",
     "iopub.status.busy": "2022-05-25T19:41:37.482598Z",
     "iopub.status.idle": "2022-05-25T19:41:37.508462Z",
     "shell.execute_reply": "2022-05-25T19:41:37.506936Z",
     "shell.execute_reply.started": "2022-05-25T19:41:37.483150Z"
    }
   },
   "outputs": [],
   "source": [
    "print(classification_report(y_test, pred_lg))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Decision Tree Classifier\n",
    "\n",
    "Decision Trees, the popular and time-tested method of applying logic to complex problems, where the variables are many and the options specific and dependent, have an important role to play within Machine Learning.\n",
    "\n",
    "We will dedicate this paper to understanding why this reasonably humble technique has become such an important tool for data scientists. And we will start the debate by suggesting that Decision Trees are popular because they have two key properties, which are: \n",
    "* Simplicity: Decision Trees are simple, visually appealing and are easy to interpret.\n",
    "* Accuracy: Advance Decision Tree models show exceptional performance in predicting patterns in complex data.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:40.517586Z",
     "iopub.status.busy": "2022-05-25T19:41:40.517034Z",
     "iopub.status.idle": "2022-05-25T19:41:40.523678Z",
     "shell.execute_reply": "2022-05-25T19:41:40.522280Z",
     "shell.execute_reply.started": "2022-05-25T19:41:40.517550Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:41.131536Z",
     "iopub.status.busy": "2022-05-25T19:41:41.131168Z",
     "iopub.status.idle": "2022-05-25T19:41:41.137385Z",
     "shell.execute_reply": "2022-05-25T19:41:41.136001Z",
     "shell.execute_reply.started": "2022-05-25T19:41:41.131505Z"
    }
   },
   "outputs": [],
   "source": [
    "# Creating object of the model\n",
    "model_dt = DecisionTreeClassifier(max_depth=4, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:41.762390Z",
     "iopub.status.busy": "2022-05-25T19:41:41.761605Z",
     "iopub.status.idle": "2022-05-25T19:41:41.794933Z",
     "shell.execute_reply": "2022-05-25T19:41:41.793833Z",
     "shell.execute_reply.started": "2022-05-25T19:41:41.762332Z"
    }
   },
   "outputs": [],
   "source": [
    "model_dt.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:43.174603Z",
     "iopub.status.busy": "2022-05-25T19:41:43.174200Z",
     "iopub.status.idle": "2022-05-25T19:41:43.180321Z",
     "shell.execute_reply": "2022-05-25T19:41:43.179391Z",
     "shell.execute_reply.started": "2022-05-25T19:41:43.174565Z"
    }
   },
   "outputs": [],
   "source": [
    "pred_dt = model_dt.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:44.374635Z",
     "iopub.status.busy": "2022-05-25T19:41:44.374097Z",
     "iopub.status.idle": "2022-05-25T19:41:44.390266Z",
     "shell.execute_reply": "2022-05-25T19:41:44.389149Z",
     "shell.execute_reply.started": "2022-05-25T19:41:44.374582Z"
    }
   },
   "outputs": [],
   "source": [
    "print(classification_report(y_test, pred_dt))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Random Forest\n",
    "\n",
    "Random forest consists of a large number of individual decision trees that operate as an ensemble. Each individual tree in the random forest spits out a class prediction and the class with the most votes becomes our model’s prediction.  \n",
    "\n",
    "The low correlation between models is the key. Uncorrelated models can produce ensemble predictions that are more accurate than any of the individual predictions. The reason for this wonderful effect is that the trees protect each other from their individual errors (as long as they don’t constantly all err in the same direction). While some trees may be wrong, many other trees will be right, so as a group the trees are able to move in the correct direction. So the prerequisites for random forest to perform well are:\n",
    "* There needs to be some actual signal in our features so that models built using those features do better than random guessing.\n",
    "* The predictions (and therefore the errors) made by the individual trees need to have low correlations with each other."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:49.403832Z",
     "iopub.status.busy": "2022-05-25T19:41:49.403243Z",
     "iopub.status.idle": "2022-05-25T19:41:49.408964Z",
     "shell.execute_reply": "2022-05-25T19:41:49.407879Z",
     "shell.execute_reply.started": "2022-05-25T19:41:49.403788Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:50.740694Z",
     "iopub.status.busy": "2022-05-25T19:41:50.740142Z",
     "iopub.status.idle": "2022-05-25T19:41:50.747474Z",
     "shell.execute_reply": "2022-05-25T19:41:50.746012Z",
     "shell.execute_reply.started": "2022-05-25T19:41:50.740651Z"
    }
   },
   "outputs": [],
   "source": [
    "model_rf = RandomForestClassifier(n_estimators=400,min_samples_leaf=0.13, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:52.692248Z",
     "iopub.status.busy": "2022-05-25T19:41:52.691864Z",
     "iopub.status.idle": "2022-05-25T19:41:54.117375Z",
     "shell.execute_reply": "2022-05-25T19:41:54.116393Z",
     "shell.execute_reply.started": "2022-05-25T19:41:52.692216Z"
    }
   },
   "outputs": [],
   "source": [
    "model_rf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:55.287640Z",
     "iopub.status.busy": "2022-05-25T19:41:55.287262Z",
     "iopub.status.idle": "2022-05-25T19:41:55.413291Z",
     "shell.execute_reply": "2022-05-25T19:41:55.411714Z",
     "shell.execute_reply.started": "2022-05-25T19:41:55.287609Z"
    }
   },
   "outputs": [],
   "source": [
    "# Making Prediction\n",
    "pred_rf = model_rf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:56.760654Z",
     "iopub.status.busy": "2022-05-25T19:41:56.760246Z",
     "iopub.status.idle": "2022-05-25T19:41:56.777441Z",
     "shell.execute_reply": "2022-05-25T19:41:56.776390Z",
     "shell.execute_reply.started": "2022-05-25T19:41:56.760618Z"
    }
   },
   "outputs": [],
   "source": [
    "print(classification_report(y_test,pred_rf))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## XGBoost\n",
    "\n",
    "Let's start with popular XGB Classifier and check it's performance. The two main reasons to use XGBoost are flexibility, execution speed and model performance. XGBoost dominates structured or tabular datasets on classification and regression predictive modeling problems. Its strength doesn’t only come from the algorithm, but also from all the underlying system optimization.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:41:59.887840Z",
     "iopub.status.busy": "2022-05-25T19:41:59.887243Z",
     "iopub.status.idle": "2022-05-25T19:42:00.671403Z",
     "shell.execute_reply": "2022-05-25T19:42:00.670381Z",
     "shell.execute_reply.started": "2022-05-25T19:41:59.887800Z"
    }
   },
   "outputs": [],
   "source": [
    "xg = XGBClassifier()\n",
    "xg.fit(X_train, y_train)\n",
    "y_test_hat_xg = xg.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:42:02.155589Z",
     "iopub.status.busy": "2022-05-25T19:42:02.155226Z",
     "iopub.status.idle": "2022-05-25T19:42:02.173443Z",
     "shell.execute_reply": "2022-05-25T19:42:02.171983Z",
     "shell.execute_reply.started": "2022-05-25T19:42:02.155556Z"
    }
   },
   "outputs": [],
   "source": [
    "print(classification_report(y_test, y_test_hat_xg))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We could try some hyperparameter tunning with models above."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deep Neural Networks\n",
    "\n",
    "Deep Neural Networks (DNN) is a neural network with some level of complexity, usually at least has two layers, qualifies as a deep neural network, or deep net for short. Deep nets process data in complex ways by employing sophisticated math modeling. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:42:06.514924Z",
     "iopub.status.busy": "2022-05-25T19:42:06.514122Z",
     "iopub.status.idle": "2022-05-25T19:42:06.520850Z",
     "shell.execute_reply": "2022-05-25T19:42:06.519604Z",
     "shell.execute_reply.started": "2022-05-25T19:42:06.514881Z"
    }
   },
   "outputs": [],
   "source": [
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Dense, Dropout, Flatten\n",
    "from tensorflow.keras.optimizers import Adam\n",
    "from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We use sequential model with multiple dense & dropout layers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:42:08.373029Z",
     "iopub.status.busy": "2022-05-25T19:42:08.372247Z",
     "iopub.status.idle": "2022-05-25T19:43:05.507087Z",
     "shell.execute_reply": "2022-05-25T19:43:05.506079Z",
     "shell.execute_reply.started": "2022-05-25T19:42:08.372983Z"
    }
   },
   "outputs": [],
   "source": [
    "model = Sequential()\n",
    "\n",
    "model.add(Dense(1024, activation='relu'))\n",
    "model.add(Dropout(0.1))\n",
    "\n",
    "model.add(Dense(1024, activation='relu'))\n",
    "model.add(Dropout(0.1))\n",
    "\n",
    "model.add(Dense(1024, activation='relu'))\n",
    "model.add(Dropout(0.1))\n",
    "\n",
    "model.add(Dense(512, activation='relu'))\n",
    "model.add(Dropout(0.2))\n",
    "\n",
    "model.add(Dense(256, activation='relu'))\n",
    "model.add(Dropout(0.25))\n",
    "\n",
    "model.add(Dense(128, activation='relu'))\n",
    "model.add(Dropout(0.45))\n",
    "\n",
    "model.add(Dense(1, activation='sigmoid'))\n",
    "\n",
    "reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.3, verbose=1,patience=10, min_lr=0.0000000001)\n",
    "early_stopping_cb = EarlyStopping(patience=10, restore_best_weights=True)\n",
    "\n",
    "model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "history = model.fit(x=X_train, y=y_train, batch_size=128, epochs=100, validation_data=(X_test, y_test), callbacks=[early_stopping_cb, reduce_lr])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Model is trained, increasing dropout solves overfitting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:43:09.892107Z",
     "iopub.status.busy": "2022-05-25T19:43:09.891552Z",
     "iopub.status.idle": "2022-05-25T19:43:10.432246Z",
     "shell.execute_reply": "2022-05-25T19:43:10.430903Z",
     "shell.execute_reply.started": "2022-05-25T19:43:09.892072Z"
    }
   },
   "outputs": [],
   "source": [
    "y_test_hat_tf = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Output of prediction are probabilities, let's convert probabilities into 0/1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:43:11.566321Z",
     "iopub.status.busy": "2022-05-25T19:43:11.565906Z",
     "iopub.status.idle": "2022-05-25T19:43:11.580401Z",
     "shell.execute_reply": "2022-05-25T19:43:11.579435Z",
     "shell.execute_reply.started": "2022-05-25T19:43:11.566286Z"
    }
   },
   "outputs": [],
   "source": [
    "y_test_hat_tf2 = [1 if x > 0.5 else 0 for x in y_test_hat_tf ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And finally checkout classification report!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2022-05-25T19:43:19.167629Z",
     "iopub.status.busy": "2022-05-25T19:43:19.167035Z",
     "iopub.status.idle": "2022-05-25T19:43:19.187769Z",
     "shell.execute_reply": "2022-05-25T19:43:19.186573Z",
     "shell.execute_reply.started": "2022-05-25T19:43:19.167592Z"
    }
   },
   "outputs": [],
   "source": [
    "print(classification_report(y_test, y_test_hat_tf2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Xgboost is slightly better than NN"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Summary  \n",
    "\n",
    "We do some testing and applies 6 algorithms for the model and we get the best accuracy from XGBoost compared to the Logistic, Regression Tree, Random Forest and DNN.  \n",
    "\n",
    "The result from the other testing also satisfied (more than 75%). It means that the result we got from the market analysis regarding churn prediction is satisfactory reliable and the result are:\n",
    "\n",
    "* Target more on young and middle-aged customers because they can adopt easily to modern tecnology and pretty much have budget to spend on the service\n",
    "* Offer extra discount for the returning customer or the one who decided to choose one or two years contract, it will make them likely to stay with the package and contract\n",
    "* Overall discout will make a big difference because price is the major factors for the customers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Recomendations and Limitations  \n",
    "\n",
    "Regarding the limitations, we should mention the following limitations from the model and also dataset.\n",
    "The number of observations are enough, but if we could have more columns of features like the customers’ geographic and location, (maybe another important data), we can get more ideas and insight compared to what we have now.  \n",
    "\n",
    "The dataset is a cross-sectional dataset, so this means that there are no time series factors inside it. The goal is to predict churn rate, thus we are good enough to have the option of contracts from monthly, one year to two years. This the best prediction we can provide to predict and make a decision for the market in the future. It has been proven by the result of algorithms that we use. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Resources\n",
    "\n",
    "1. Kaggle: https://www.kaggle.com/mytymohan/teleco-customer-churn-analysis\n",
    "2. https://www.kaggle.com/chinmaybgaikwad/customer-churn-in-telcos\n",
    "3. Dataset: https://www.kaggle.com/blastchar/telco-customer-churn\n",
    "4. Original dataset from IBM: https://www.ibm.com/docs/en/cognos-analytics/11.1.0?topic=samples-telco-customer-churn\n",
    "5. https://mode.com/blog/violin-plot-examples/\n",
    "6. https://towardsdatascience.com/understanding-random-forest-58381e0602d2\n",
    "7. https://towardsdatascience.com/xgboost-fine-tune-and-optimize-your-model-23d996fab663\n"
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
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
