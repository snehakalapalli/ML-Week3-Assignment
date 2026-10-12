# Week 3 Machine Learning Assignment: Iris Flower Clustering Project
# Language: Python 3

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


def main():
    print("=" * 50)
    print("   IRIS FLOWER CLUSTERING PROJECT (K-Means & PCA)")
    print("=" * 50)

    # 1. Load Iris Dataset
    iris = load_iris()
    X = iris.data
    y_true = iris.target  # True labels for comparison

    print(f"\n📊 Dataset shape: {X.shape}")

    # 2. Apply K-Means Clustering (k=3)
    print("\n🔄 Applying K-Means Clustering (k=3)...")
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    y_kmeans = kmeans.fit_predict(X)

    # 3. Cluster Centers print cheyadam
    print("\n📍 Cluster Centers:")
    print(kmeans.cluster_centers_)

    # 4. Apply PCA to reduce dataset dimensions to 2D for visualization
    print("\n📉 Applying PCA for dimensionality reduction (4D -> 2D)...")
    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X)

    # Explained variance ratio
    explained_variance = pca.explained_variance_ratio_
    print(
        f"📊 Explained Variance Ratio: {explained_variance[0]*100:.2f}% (PC1) and {explained_variance[1]*100:.2f}% (PC2)"
    )

    # 5. Visualize Clusters using Matplotlib (Scatter Plot)
    print("\n📈 Generating cluster visualization scatter plot...")
    plt.figure(figsize=(8, 6))
    plt.scatter(
        X_reduced[:, 0],
        X_reduced[:, 1],
        c=y_kmeans,
        cmap="viridis",
        edgecolors="k",
        s=50,
    )
    plt.title("K-Means Clustering on Iris Dataset (PCA Reduced to 2D)")
    plt.xlabel("Principal Component 1 (PC1)")
    plt.ylabel("Principal Component 2 (PC2)")
    plt.grid(True)

    # Save plot as an image file
    plot_filename = "iris_clusters_plot.png"
    plt.savefig(plot_filename)
    print(f"✅ Scatter plot successfully saved as '{plot_filename}'.")

    # Show plot if running locally
    # plt.show()

    print(
        "\n🙏 Iris Flower Clustering Project execution completed successfully!"
    )


if __name__ == "__main__":
    main()
  
