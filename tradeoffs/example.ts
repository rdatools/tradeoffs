
export function plotWidth(designSize: MA.DW): number
{
    return designSize <= MA.DW.MEDIUM ? Math.max(window.innerWidth - 220, 375) :
        designSize <= MA.DW.MEDIUMPLUS ? 650 : 700;
}
export function plotWidth(designSize: MA.DW): number
{
    return designSize <= MA.DW.MEDIUM ? Math.max(window.innerWidth - 220, 375) :
        designSize <= MA.DW.MEDIUMPLUS ? 650 : 700;
}

// A box plot modelled on this - https://plotly.com/javascript/box-plots/#fully-styled-box-plot
renderBoxPlot(): void
    {
        const {bHidePartisanData} = this.props;
        const {openPickMapDialog} = this.state;

        if(openPickMapDialog || !this.profile || !this.scorecard)
{
    const boxPlotDiv = document.getElementById('box-plot');
    boxPlotDiv.innerHTML = '';
    return;
}

if (!document.getElementById('box-plot'))
    return;

const mapID = 'some map identifier';  // The current map
const allRatings = this.getAllRatings();
if (!(allRatings && allRatings.length >= 5))
    return;     // May not have sessions yet

if (allRatings[0].length < this.MIN_BOXPLOT_COMPARISON_MAPS)
    return;

let boxplotTraces = [];
let boxplotLayout = {};
let boxplotConfig = {};

{
    const diagramWidth = AU.plotWidth(this.props.designSize);

    const xData = bHidePartisanData ?
        [
            AU.Ratings.equitable.label,
            AU.Ratings.compact.label,
            AU.Ratings.cohesive.label
        ] :
        [
            AU.Ratings.unbiased.label,
            AU.Ratings.competitive.label,
            AU.Ratings.equitable.label,
            AU.Ratings.compact.label,
            AU.Ratings.cohesive.label
        ]

    const yData = bHidePartisanData ?
        [
            allRatings[AU.Rating.MinorityRights],
            allRatings[AU.Rating.Compactness],
            allRatings[AU.Rating.Splitting]
        ] :
        [
            allRatings[AU.Rating.Proportionality],
            allRatings[AU.Rating.Competitiveness],
            allRatings[AU.Rating.MinorityRights],
            allRatings[AU.Rating.Compactness],
            allRatings[AU.Rating.Splitting]
        ];

    for (var i = 0; i < xData.length; i++)
    {
        var trace = {
            type: 'box',
            y: yData[i],
            name: xData[i],
            boxpoints: 'all',
            jitter: 0.5,
            whiskerwidth: 0.2,
            fillcolor: 'cls',
            marker: {
                size: 2,
                symbol: 'circle'
            },
            line: {
                width: 1
            },
            selectedpoints: [0],  // Highlight the current map's ratings
            selected: {
                marker: {
                    size: 5,
                    color: 'black'
                }
            }
        };
        boxplotTraces.push(trace);
    };

    boxplotLayout = {
        // title: 'Ratings Compared to Similar Maps',
        width: diagramWidth,
        yaxis: {
            range: [0, 100],
            // autorange: true,
            showgrid: true,
            zeroline: true,
            dtick: 5,
            gridcolor: 'rgb(255, 255, 255)',
            gridwidth: 1,
            zerolinecolor: 'rgb(255, 255, 255)',
            zerolinewidth: 2
        },
        margin: {
            l: 40,
            r: 30,
            b: 80,
            t: 100
        },
        showlegend: false,
        paper_bgcolor: bgcolor,
        plot_bgcolor: bgcolor
    };
}

boxplotConfig = {
    toImageButtonOptions: {
        format: 'png', // one of png, svg, jpeg, webp
        filename: 'box-plot'
    },
    // Remove all the plotly hover commands, except download
    modeBarButtonsToRemove: ['zoom2d', 'select2d', 'lasso2d', 'autoScale2d', 'toggleSpikelines', 'hoverClosestCartesian', 'hoverCompareCartesian'],
    displayModeBar: true,
    displaylogo: false,
    responsive: true
};

Plotly.newPlot('box-plot', boxplotTraces, boxplotLayout, boxplotConfig);
  }
