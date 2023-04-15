import pandas as pd
import matplotlib.pyplot as plt


def main():
    game_statistics = pd.read_csv("gl2022.txt", header=None)
    innings = 7
    games = 900
    recorded = 0
    runs_home = [0] * innings
    runs_away = [0] * innings
    runs_per_inning = 0
    # for g in range(0, len(game_statistics)):
    for g in range(0, games):
        if len(game_statistics.loc[g, 19]) >= innings and len(game_statistics.loc[g, 20]) >= innings:
            recorded += 1
            for i in range(0, innings):
                runs_home[i] += int(game_statistics.loc[g, 19][i])
                runs_away[i] += int(game_statistics.loc[g, 20][i])
    for i in range(0, innings):
        runs_per_inning += (runs_home[i] + runs_away[i]) / (recorded * 2)
    runs_per_inning /= innings
    print('Avg runs per inning across all innings: ' + "{:.3f}".format(runs_per_inning))
    for i in range(0, innings):
        runs_home[i] /= recorded
        print('Avg home team runs in inning ' + str(i + 1) + ': \t' + "{:.3f}".format(runs_home[i]))
        runs_away[i] /= recorded
        print('Avg away team runs in inning ' + str(i + 1) + ': \t' + "{:.3f}".format(runs_away[i]))
    innings = [1, 2, 3, 4, 5, 6, 7]
    avg_runs = [runs_per_inning] * 7
    plt.plot(innings, runs_home, label='HOME')
    plt.plot(innings, runs_away, label='AWAY')
    plt.plot(innings, avg_runs, label='AVG')
    plt.xlabel("Inning")
    plt.ylabel("Avg Runs")
    plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    main()
