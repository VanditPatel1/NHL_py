

rink_shapes = list()


outer_rect = dict(
            type='rect',
            xref='x',
            yref='y',
            x0='-250',
            y0='0',
            x1='250',
            y1='516.2',
            line=dict(
                width=1,
            )
)
rink_shapes.append(outer_rect)

outer_line = dict(
            type='line',
            xref='x',
            yref='y',
            x0='200',
            y0='580',
            x1='-200',
            y1='580',
            line=dict(
                width=1,
            )
)
rink_shapes.append(outer_line)

outer_arc1 = dict(
            type='path',
            xref='x',
            yref='y',
            path='M 200 580 C 217 574, 247 532, 250 516.2',
            line=dict(
                width=1,
            )
)
rink_shapes.append(outer_arc1)

outer_arc2 = dict(
            type='path',
            xref='x',
            yref='y',
            path='M -200 580 C -217 574, -247 532, -250 516.2',
            line=dict(
                width=1,
            )
)
rink_shapes.append(outer_arc2)

center_red_line = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-250',
            y0='0',
            x1='250',
            y1='0',
            line=dict(
                width=1,
                color='rgba(255, 0, 0, 1)'
            )
)
rink_shapes.append(center_red_line)

end_line = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-250',
            y0='516.2',
            x1='250',
            y1='516.2',
            line=dict(
                width=1,
                color='rgba(255, 0, 0, 1)'
            )
)
rink_shapes.append(end_line)

blue_line_shape = dict(
            type='rect',
            xref='x',
            yref='y',
            x0='250',
            y0='150.8',
            x1='-250',
            y1='155', #'-145',
            line=dict(
                color='rgba(0, 0, 255, 1)',
                width=1
            ),
            fillcolor='rgba(0, 0, 255, 1)'
)
rink_shapes.append(blue_line_shape)

center_blue_spot = dict(
            type='circle',
            xref='x',
            yref='y',
            x0='2.94',
            y0='2.8',
            x1='-2.94',
            y1='-2.8',
            line=dict(
                color='rgba(0, 0, 255, 1)',
                width=1
            ),
            fillcolor='rgba(0, 0, 255, 1)'
)
rink_shapes.append(center_blue_spot)

red_spot1_top = dict(
            type='circle',
            xref='x',
            yref='y',
            x0='135.5',
            y0='121.8',
            x1='123.5',
            y1='110.2',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            ),
            fillcolor='rgba(255, 0, 0, 1)'
)
rink_shapes.append(red_spot1_top)

red_spot2_top = dict(
            type='circle',
            xref='x',
            yref='y',
            x0='-135.5',
            y0='121.8',
            x1='-123.5',
            y1='110.2',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            ),
            fillcolor='rgba(255, 0, 0, 1)'
)
rink_shapes.append(red_spot2_top)

red_spot1_circle = dict(
            type='circle',
            xref='x',
            yref='y',
            x0='217.6',
            y0='487.2',
            x1='41.2',
            y1='313.2',
            line=dict(
                width=1,
                color='rgba(255, 0, 0, 1)'
            )
)
rink_shapes.append(red_spot1_circle)

red_spot2_circle = dict(
            type='circle',
            xref='x',
            yref='y',
            x0='-217.6',
            y0='487.2',
            x1='-41.2',
            y1='313.2',
            line=dict(
                width=1,
                color='rgba(255, 0, 0, 1)'
            )
)
rink_shapes.append(red_spot2_circle)

parallel_line1_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='230',
            y0='416.4',
            x1='217.8',
            y1='416.4',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line1_right)

parallel_line2_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='230',
            y0='384',
            x1='217.8',
            y1='384',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line2_right)

parallel_line3_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='28.8',
            y0='416.4',
            x1='41',
            y1='416.4',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line3_right)

parallel_line4_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='28.8',
            y0='384',
            x1='41',
            y1='384',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line4_right)

parallel_line1_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-230',
            y0='416.4',
            x1='-217.8',
            y1='416.4',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line1_left)

parallel_line2_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-230',
            y0='384',
            x1='-217.8',
            y1='384',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line2_left)

parallel_line3_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-28.8',
            y0='416.4',
            x1='-41',
            y1='416.4',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line3_left)

parallel_line4_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-28.8',
            y0='384',
            x1='-41',
            y1='384',
            line=dict(
                color='rgba(255, 0, 0, 1)',
                width=1
            )
)
rink_shapes.append(parallel_line4_left)

faceoff_line1_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='141.17',
            y0='423.4',
            x1='141.17',
            y1='377',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line1_right)

faceoff_line2_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='117.62',
            y0='423.4',
            x1='117.62',
            y1='377',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line2_right)

faceoff_line3_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='153',
            y0='406',
            x1='105.8',
            y1='406',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line3_right)

faceoff_line4_right = dict(
            type='line',
            xref='x',
            yref='y',
            x0='153',
            y0='394.4',
            x1='105.8',
            y1='394.4',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line4_right)

faceoff_line1_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-141.17',
            y0='423.4',
            x1='-141.17',
            y1='377',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line1_left)

faceoff_line2_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-117.62',
            y0='423.4',
            x1='-117.62',
            y1='377',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line2_left)

faceoff_line3_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-153',
            y0='406',
            x1='-105.8',
            y1='406',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line3_left)

faceoff_line4_left = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-153',
            y0='394.4',
            x1='-105.8',
            y1='394.4',
            line=dict(
                color='rgba(10, 10, 100, 1)',
                width=1
            )
)
rink_shapes.append(faceoff_line4_left)

goal_line_back_1 = dict(
            type='line',
            xref='x',
            yref='y',
            x0='64.7',
            y0='516.2',
            x1='82.3',
            y1='580',
            line=dict(
                width=1
            )
)
rink_shapes.append(goal_line_back_1)

goal_line_back_2 = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-64.7',
            y0='516.2',
            x1='-82.3',
            y1='580',
            line=dict(
                width=1
            )
)
rink_shapes.append(goal_line_back_2)

goal_line_front_1 = dict(
            type='line',
            xref='x',
            yref='y',
            x0='23.5',
            y0='516.2',
            x1='23.5',
            y1='493',
            line=dict(
                width=1
            )
)
rink_shapes.append(goal_line_front_1)

goal_line_front_2 = dict(
            type='line',
            xref='x',
            yref='y',
            x0='-23.5',
            y0='516.2',
            x1='-23.5',
            y1='493',
            line=dict(
                width=1
            )
)
rink_shapes.append(goal_line_front_2)

goal_arc1 = dict(
            type='path',
            xref='x',
            yref='y',
            path='M 23.5 493 C 20 480, -20 480, -23.5 493',
            line=dict(
                width=1,
            )
)
rink_shapes.append(goal_arc1)

goal_arc2 = dict(
            type='path',
            xref='x',
            yref='y',
            path='M 17.6 516.2 C 15 530, -15 530, -17.6 516.2',
            line=dict(
                width=1
            )
)
rink_shapes.append(goal_arc2)

referee_crease = dict(
            type='path',
            xref='x',
            yref='y',
            path='M ',
            line=dict(
                width=1,
                color='rgba(255, 0, 0, 1)'
            )
)
rink_shapes.append(referee_crease)
