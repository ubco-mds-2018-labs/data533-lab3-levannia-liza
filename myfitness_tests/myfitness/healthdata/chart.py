def chart(columnX, columnY, xlabel, ylabel):
    """Create an interactive bar graph using pygal
        Parameters: columnX as list of strings, columnY as list of values, xlabel as string, ylabel as string
        
        Return: .svg file with xlabel, ylabel and title"""
    
    # import pygal, import SVG, and display from IPython.display
    import pygal 
    from IPython.display import SVG, display

    # assign lists provided to chart axises
    y = columnY
    x = columnX
    
    # construct pygal bar chart
    bar_chart = pygal.Bar(include_x_axis=True)
    bar_chart.add(ylabel,y)
    bar_chart.title = 'My Fitness Chart'
    bar_chart.x_labels = x
    bar_chart.x_title = xlabel
    bar_chart.y_title = ylabel

    # render bar chart to file and brower for viewing
    bar_chart.render_to_file('my_fitness_data.svg')

    bar_chart.render_in_browser()
