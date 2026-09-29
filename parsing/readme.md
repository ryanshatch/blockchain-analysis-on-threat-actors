<!-- case-visual:start -->
<p align="center">
  <img src="../assets/readme-headers/parsing.svg" alt="Transaction parsing tools — File merging, structured records and data-loss analysis" width="1200">
</p>
<!-- case-visual:end -->

<!-- doc-nav:start -->
<p><a href="../readme.md">Home</a> · <a href="../wallets.md">Wallet index</a> · <a href="../CATALOG.md">All case files</a></p>
<!-- doc-nav:end -->

# Parsing from solscan

<!-- contents:start -->
<details>
<summary>Contents</summary>
<ul>
<li><a href="#section-overview">Overview</a></li>
<li><a href="#section-repository-structure">Repository Structure</a></li>
<li><a href="#section-getting-started">Getting Started</a></li>
<li><a href="#section-license">License</a></li>
</ul>
</details>
<!-- contents:end -->

<a id="section-overview"></a>
## Overview
This repository contains tools for parsing and merging various file types, particularly focusing on CSV files. It provides a graphical user interface (GUI) for easy file merging and visualizing data loss.

<a id="section-repository-structure"></a>
## Repository Structure
- **sol tx history/**: Directory containing historical transaction data.
- **combined_sol_transfers.txt**: Combined text file of SOL transfers.
- **combined_values.csv**: Combined CSV file of values.
- **merge_files.py**: Script to merge various file types into one.
- **visual_of_data_loss.py**: Script to visualize data loss.

<a id="section-getting-started"></a>
## Getting Started

### Prerequisites
- Python 3.x with Tk support (Tkinter comes with many Python distributions; on Debian/Ubuntu install `python3-tk` through your OS package manager).
- Required libraries:
    ```sh
    python -m pip install pandas matplotlib seaborn python-docx
    ```

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ryanshatch/blockchain-analysis-on-threat-actors.git
    ```
2. Navigate to the `parsing` directory:
    ```sh
    cd blockchain-analysis-on-threat-actors/parsing
    ```

### Usage

#### File Merger
1. Run the `merge_files.py` script to open the GUI:
    ```sh
    python merge_files.py
    ```
2. Use the GUI to:
   - Browse and select multiple files to combine.
   - Enter a name for the new combined file.
   - Click "CREATE" to merge the selected files into one.
   - The merger writes one `.txt` file. The visualization utility writes CSV-formatted content with a `.txt` extension and displays a missing-value heatmap; it does not calculate financial losses.

#### Visualize Data Loss
1. Run the `visual_of_data_loss.py` script to visualize data loss:
    ```sh
    python visual_of_data_loss.py
    ```

<a id="section-license"></a>
## License
This project was developed and is under copyright by Ryan Hatch