\ Model Furniture
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  45 make[chairs] + 80 make[tables] - 20 extra[mahogany] - 30 extra[labor]
Subject To
 r[mahogany]: 5 make[chairs] + 20 make[tables] - extra[mahogany] <= 400
 r[labor]: 10 make[chairs] + 15 make[tables] - extra[labor] <= 450
 B: 45 make[chairs] + 80 make[tables] >= 4500
Bounds
End
