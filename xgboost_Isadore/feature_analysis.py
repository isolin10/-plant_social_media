#feature_analysis.py

from xgboost import XGBRegressor
import numpy as np
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

def perform_feature_analysis(train_data, target_column, feature_names):
    """
    使用XGBoost進行特徵重要性分析，返回特徵重要性和前三高相關特徵名稱及索引
    """
    X_train = np.delete(train_data, target_column, axis=1)  # 移除目標列
    y_train = train_data[:, target_column]  # 目標列

    model = XGBRegressor()
    model.fit(X_train, y_train)
    feature_importances = model.feature_importances_

    # 將特徵名稱與重要性配對
    feature_importance_dict = dict(zip(feature_names, feature_importances))
    feature_importance_df = pd.DataFrame(
        list(feature_importance_dict.items()), 
        columns=["Feature", "Importance"]
    ).sort_values(by="Importance", ascending=False)

    # 獲取前三高相關特徵名稱及其索引
    top_features = feature_importance_df.head(3)
    top_feature_names = top_features["Feature"].tolist()
    top_feature_indices = [feature_names.index(name) for name in top_feature_names]

    # 繪製特徵重要性圖 Xgboost會依照'weight', 'gain', 'cover'的重要性 去篩選出重要的特徵#
    xgb.plot_importance(model, importance_type='weight')  # 可選 'weight', 'gain', 'cover'
    plt.show()
    xgb.plot_importance(model, importance_type='gain')  # 可選 'weight', 'gain', 'cover'
    plt.show()
    xgb.plot_importance(model, importance_type='cover')  # 可選 'weight', 'gain', 'cover'
    plt.show()
    
    return feature_importance_df, top_feature_indices
