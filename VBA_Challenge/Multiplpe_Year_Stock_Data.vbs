'Create a script that loops through all the stocks for one year
'   and outputs the following information:
'   -The ticker symbol
'   -Yearly change from the opening price at the beginning of a
'    given year to the closing price at the end of that year.
'   -The percentage change from the opening price at the beginning
'    of a given year to the closing price at the end of that year.
'   -The total stock volume of the stock.
'   -Add functionality to your script to return the stock with the
'    "Greatest % increase", "Greatest % decrease", and "Greatest total volume".
'   -Make the appropriate adjustments to your VBA script to enable
'    it to run on every worksheet (that is, every year) at once.

Sub Multiple_year_stock():
    For Each ws In Worksheets
        ' Find the total number of rows nad the last ros index
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        
        ' Set the required headers
        ws.Range("I1") = "Tikcer"
        ws.Range("P1") = "Tikcer"
        ws.Range("Q1") = "Value"
        ws.Range("J1") = "Yearly Change"
        ws.Range("K1") = "Percent Change"
        ws.Range("L1") = "Total Stock Volume"
        ws.Range("O2") = "Greatest % increase"
        ws.Range("O3") = "Greatest % decrease"
        ws.Range("O4") = "Greatest total volume"
        
        ' Declare required variables
        Dim WorksheetName As String
        Dim TickerIdx As Integer ' Index of the Ticker
        Dim Openning As Double ' Holds value of the <open>
        Dim Closing As Double ' Holds value of the <close>
        Dim Vloume As Double ' Holds value of the <volume>
        Dim GreatInc As Double ' Holds value of the <Greatest % increase>
        Dim GITicker As String ' Ticker name with the <Greatest % increase>
        Dim GreatDec As Double ' Holds value of the <Greatest % Decrease>
        Dim GDTicker As String ' Ticker name with the <Greatest % Decrease>
        Dim GreatTotal As Double ' Holds value of the <Greatest Total Volume>
        Dim GTTicker As String ' Ticker name with the <Greatest Total Volume>
        
        'Initializing values to variables
        WorksheetName = ws.Name
        TickerIdx = 2
        Openning = ws.Cells(2, 3).Value
        Closing = ws.Cells(2, 6).Value
        volume = 0
        GreatInc = 0
        GreatDec = 0
        GreatTotal = 0
        ws.Range("I2") = ws.Cells(2, 1).Value
        
        For i = 2 To LastRow
            ' If stil the same ticker
            If ws.Cells(i, 1).Value = ws.Cells(i + 1, 1).Value Then
                ' Update volume
                volume = ws.Range("G" & i).Value + volume
            ' If Ticker name changes
            Else
                ' Update the Total Volume for Ticker and reset the Volume
                volume = ws.Range("G" & i).Value + volume
                ws.Range("L" & TickerIdx) = volume
                volume = 0
                
                ' Update Closing and calculate the yearly and percent change
                Closing = ws.Range("F" & i).Value
                ws.Range("J" & TickerIdx) = Closing - Openning
                ws.Range("K" & TickerIdx) = FormatPercent((Closing / Openning) - 1)
                
                '' color the interior
                ' green if yearly change is positive
                If ws.Range("J" & TickerIdx).Value > 0 Then
                    ws.Range("J" & TickerIdx).Interior.ColorIndex = 4
                ' no color if yearly change is zero
                ElseIf ws.Range("J" & TickerIdx).Value = 0 Then
                    ws.Range("J" & TickerIdx).Interior.ColorIndex = 0
                ' red if yearly change is negative
                Else
                    ws.Range("J" & TickerIdx).Interior.ColorIndex = 3
                End If
                
                ' increment the index of the ticker
                TickerIdx = TickerIdx + 1
                ws.Range("I" & TickerIdx) = ws.Cells(i + 1, 1).Value
                
                ' Updating the Openning value
                Openning = ws.Cells(i + 1, 3).Value
            End If
        Next i
        
        ' Calculate max % increase, decrease and max total volume
        LRTicker = ws.Cells(Rows.Count, 9).End(xlUp).Row ' Last row of the Tickers
        Rng = ws.Range("K2:K" & LRTicker) ' Range of the percent Change
        RngTotal = ws.Range("L2:L" & LRTicker) ' Range of the Total Stock Volume
        GreatInc = WorksheetFunction.Max(Rng)
        GreatDec = WorksheetFunction.Min(Rng)
        GreatTotal = WorksheetFunction.Max(RngTotal)
        GITicker = ws.Range("I" & WorksheetFunction.Match(GreatInc, Rng, 0) + 1)
        GDTicker = ws.Range("I" & WorksheetFunction.Match(GreatDec, Rng, 0) + 1)
        GTTicker = ws.Range("I" & WorksheetFunction.Match(GreatTotal, RngTotal, 0) + 1)
        
        ws.Range("P2") = GITicker
        ws.Range("P3") = GDTicker
        ws.Range("P4") = GTTicker
        ws.Range("Q2") = FormatPercent(GreatInc)
        ws.Range("Q3") = FormatPercent(GreatDec)
        ws.Range("Q4") = Format(GreatTotal, "Scientific")
    Next ws
    
End Sub



