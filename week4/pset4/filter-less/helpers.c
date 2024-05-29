#include "helpers.h"
#include <math.h>
#include <stdio.h>

#define RED_COLOR 0
#define GREEN_COLOR 1
#define BLUE_COLOR 2


void swap(RGBTRIPLE *a, RGBTRIPLE *b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float original_average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            int rgbGray = round(original_average);
            image[i][j].rgbtRed = rgbGray;
            image[i][j].rgbtGreen = rgbGray;
            image[i][j].rgbtBlue = rgbGray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed = 0;
    int sepiaGreen = 0;
    int sepiaBlue = 0;

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            sepiaRed = round( .393 * image[row][column].rgbtRed + .769 * image[row][column].rgbtGreen + .189 * image[row][column].rgbtBlue);
            sepiaGreen = round( .349 * image[row][column].rgbtRed + .686 * image[row][column].rgbtGreen + .168 * image[row][column].rgbtBlue);
            sepiaBlue = round( .272 * image[row][column].rgbtRed + .534 * image[row][column].rgbtGreen + .131 * image[row][column].rgbtBlue);

            image[row][column].rgbtRed = fmin(255, sepiaRed);
            image[row][column].rgbtGreen = fmin(255, sepiaGreen);
            image[row][column].rgbtBlue = fmin(255, sepiaBlue);
       }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < (width / 2); column++)
        {
            temp = image[row][column];
            image[row][column] = image[row][width - column - 1];
            image[row][width - column - 1] = temp;
        }
    }
    return;
}

int getBlur(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_position)
{
    float count = 0;
    int sum = 0;
    for (int row = i - 1; row <= (i + 1); row++)
    {
        for (int column = j -1; column <= (j + 1); column++)
        {
            if (row < 0 || row >= height || column < 0 || column >= width)
            {
                continue;
            }
            if (color_position == RED_COLOR)
            {
                sum += image[row][column].rgbtRed;
            }
            else if (color_position == GREEN_COLOR)
            {
                sum += image[row][column].rgbtGreen;
            }
            else
            {
                sum += image[row][column].rgbtBlue;
            }
            count++;
        }
    }
    return round(sum/count);
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Do a box blur = compute the new value for a pixel by taking the average of the old color values
    //of all 9 pixels that forms a grid around that original pixel
    //(= all the pixels that are within one row and one column of the original pixel)
    //Whenever on the edge, you will compute 6 values
    //Whenever on the corner, you will compute only 4 pixels;
    //Calculate the averga amount of red, blue, green of the grid;
    RGBTRIPLE copy[height][width];

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            copy[row][column] = image[row][column];
        }
    }
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
           image[row][column].rgbtRed = getBlur(row, column, height, width, copy, RED_COLOR);
           image[row][column].rgbtGreen = getBlur(row, column, height, width, copy, GREEN_COLOR);
           image[row][column].rgbtBlue = getBlur(row, column, height, width, copy, BLUE_COLOR);
        }
    }
    return;
}

void swap(RGBTRIPLE *a, RGBTRIPLE *b)
{
    RGBTRIPLE tmp = *a;
    *a = *b;
    *b = tmp;
}