import matplotlib.pyplot as plt
import os

def set_netflix_style():
    plt.rcParams.update({
        "figure.facecolor": "#141414",
        "axes.facecolor":   "#141414",
        "axes.edgecolor":   "#FFFFFF",
        "axes.labelcolor":  "#FFFFFF",
        "xtick.color":      "#FFFFFF",
        "ytick.color":      "#FFFFFF",
        "text.color":       "#FFFFFF",
        "grid.color":       "#2a2a2a",
        "font.size":        12,
    })

def save_figure(filename):
    os.makedirs("outputs/figures", exist_ok=True)
    plt.savefig(f"outputs/figures/{filename}")  # what goes here?

def plot_bar(data, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(data.index, data.values)        # what are the two inputs?
    ax.set_title(title)       # what goes here?
    ax.set_xlabel(xlabel)      # what goes here?
    ax.set_ylabel(ylabel)      # what goes here?

def plot_line(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(x,y, linewidth=2.5)  # what are x and y?
    ax.set_title(title)       # what goes here?
    ax.set_xlabel(xlabel)      # what goes here?
    ax.set_ylabel(ylabel)      # what goes here?

if __name__ == "__main__":
    from data_loader import load_netflix_data

    df = load_netflix_data()
    set_netflix_style()

    # Test bar chart
    data = df['type'].value_counts()
    plot_bar(
        data   = data,
        title  = "Movies vs TV Shows on Netflix",
        xlabel = "Number of Titles",
        ylabel = "Content Type"
    )
    save_figure("content_type.png")
    plt.show()