$(function () {
    $('#container').highcharts({
        chart: {
            type: 'bar',
              style: {
           		fontFamily:'FaktPro, Helvetica, arial, sans-serif',

           }
        },
        title: {
        	align: 'left',
            text: 'TKTK'
        },
        subtitle: {
            text: ''
        },
        legend: {
        	 align: 'right',
    		verticalAlign: 'top',
    		y: 20
        },
        exporting: {
        	enabled: false
        },
        credits: {
        	enabled: false
        },
        xAxis: {
            categories: [
                'Have a good <br> work/life balance',
                'Experienced sexual <br> discrimination in <br> the past year',
                'Experienced direct <br> discrimination in <br> the past year',
                'Experienced indirect <br> discrimination in <br> the past year',
                'Experienced bullying <br> in the past year',
                'Experienced sexual <br> harassment in <br> the past year',
            ],
            crosshair: true
        },
        yAxis: {
            labels: {
            formatter: function () {
                return this.value + '%' ;
            }
        },
            min: 0,
            ceiling: 100,
            title: {
                text: 'Percent of Respondents',



            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:1f}% </b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0,
                borderWidth: 0
            }
        },
        series: [{
            name: 'TK1',
            color: '#bdbdbd',
            data: [59, 32, 21, 18, 28, 14]



        }, {
            name: 'TK2',
            color: '#5e5e5e',
            data: [69, 3, 4, 5, 15, 2]

        }]
    });
});
//]]>
