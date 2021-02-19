import numpy as np
import pandas as pd
from janitor.chemistry import morgan_fingerprint
import pickle


act = {
  1: "blocker",
  0: "non-blocker",
}

# load the input molecule
smi = [['Fc1ccc(cc1)Cn2c5ccccc5nc2NC4CCN(CCc3ccc(OC)cc3)CC4']]
df = pd.DataFrame(smi, columns = ['smiles'])
morgan_df =morgan_fingerprint(df=df.smiles2mol('smiles', 'mols'),mols_column_name='mols',kind='bits')
df = df.join(morgan_df)
X_test = df.iloc[:,2:]

# RF model
pkl_file = open('rf.pkl', 'rb')
model = pickle.load(pkl_file)
y_pred = model.predict(X_test)
y_pred = y_pred[0]
y_pred_prob = model.predict_proba(X_test).T[1]
y_pred_prob = y_pred_prob.ravel()
y_pred_prob = np.round(y_pred_prob, 2)
y_pred_prob = y_pred_prob[0]

pkl_file.close()
print('RF Pred:\t%s\t(%.2f)' % (act[y_pred], y_pred_prob))

# XGB model
pkl_file = open('xgb.pkl', 'rb')
model = pickle.load(pkl_file)

y_pred = model.predict(X_test)
y_pred = y_pred[0]
y_pred_prob = model.predict_proba(X_test).T[1]
y_pred_prob = y_pred_prob.ravel()
y_pred_prob = np.round(y_pred_prob, 2)
y_pred_prob = y_pred_prob[0]

pkl_file.close()
print('XGB Pred:\t%s\t(%.2f)' % (act[y_pred], y_pred_prob))