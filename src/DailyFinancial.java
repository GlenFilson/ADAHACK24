import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;

public class DailyFinancial {
    private static JPanel mainPanel;
    private JPanel panel1;
    private JPanel panel2;
    private static CardLayout cardLayout;
    private JPanel[] questionPanels;
    static int numberOfQuestions;
    static JLabel graph;
    static ArrayList<String> question;
    static ArrayList<String> option1;
    static ArrayList<String> option2;
    static ArrayList<Integer> option1cost;
    static ArrayList<Integer> option2cost;
    static int totalSpent;
    static int counter;
    ImageIcon image;

    public DailyFinancial() {
        counter = 0;
        readCSV();

        cardLayout = new CardLayout();

        mainPanel = new JPanel(cardLayout);

        panel1 = new JPanel(cardLayout);
        panel1.setPreferredSize(new Dimension(640, 510));

        panel2 = new JPanel(new BorderLayout());
        panel2.setPreferredSize(new Dimension(640, 510));
        JLabel label = new JLabel("Your Savings Projection over 10 Years");
        label.setPreferredSize(new Dimension(640, 50));
        label.setFont(new Font("Arial", Font.BOLD, 20));
        label.setHorizontalAlignment(0);
        panel2.add(label, BorderLayout.NORTH);
        graph = new JLabel();
        graph.setPreferredSize(new Dimension(640, 510));
        ImageIcon image = new ImageIcon("C:\\Users\\GlenF\\IdeaProjects\\test\\tenyears.jpg");
        graph.setIcon(image);
        panel2.add(graph, BorderLayout.CENTER);

        mainPanel.add(panel1, "Question Panels");
        mainPanel.add(panel2, "Completion Panel");

        questionPanels = new JPanel[numberOfQuestions];
        for (int i = 0; i < questionPanels.length; i++) {
            questionPanels[i] = createPanel(i);
            panel1.add(questionPanels[i], "Card" + i);
        }
    }

    public static void readCSV() {
        question = new ArrayList<>();
        option1 = new ArrayList<>();
        option1cost = new ArrayList<>();
        option2 = new ArrayList<>();
        option2cost = new ArrayList<>();
        String csvFile = "C:\\Users\\GlenF\\IdeaProjects\\AdaHack24\\Lib\\child.csv";
        String line = "";
        String csvSplitBy = ",";
        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                String[] entry = line.split(csvSplitBy);
                question.add(entry[0]);
                option1.add(entry[1]);
                option1cost.add(Integer.parseInt(entry[2].trim()));
                option2.add(entry[3]);
                option2cost.add(Integer.parseInt(entry[4].trim()));
            }
            numberOfQuestions = question.size();  // Move outside of catch block to ensure proper initialization
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private JPanel createPanel(int i) {
        JPanel panel = new JPanel();
        JLabel questionLabel = new JLabel(question.get(i));
        questionLabel.setPreferredSize(new Dimension(640, 50));
        questionLabel.setHorizontalAlignment(0);
        questionLabel.setFont(new Font("Arial", Font.BOLD, 30));
        JButton question1Button = new JButton(option1.get(i) + " (£" + option1cost.get(i) + ")");
        question1Button.setPreferredSize(new Dimension(300, 80));
        question1Button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                totalSpent += option1cost.get(i);
                showNextCard();
            }
        });
        JButton question2Button = new JButton(option2.get(i) + " (£" + option2cost.get(i) + ")");
        question2Button.setPreferredSize(new Dimension(300, 80));
        question2Button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                totalSpent += option2cost.get(i);
                showNextCard();
            }
        });
        panel.add(questionLabel);
        panel.add(question1Button);
        panel.add(question2Button);
        return panel;
    }

    private void showNextCard() {
        counter++;
        if (counter >= numberOfQuestions) {
            WriteCSV();
            executePy();
            try {
                Image image = ImageIO.read(new File("C:\\Users\\GlenF\\IdeaProjects\\AdaHack24\\Lib\\tenyears.jpg"));
                ImageIcon newImageIcon = new ImageIcon(image);
                graph.setIcon(newImageIcon);
                graph.revalidate();
                graph.repaint();
            } catch (IOException ex) {
                ex.printStackTrace();
            }


            cardLayout.show(mainPanel, "Completion Panel");
        } else {
            cardLayout.next(panel1);
        }
        System.out.println(counter);
        System.out.println(numberOfQuestions);
    }

    private void revalidate() {
        mainPanel.revalidate();
        mainPanel.repaint();
    }

    public static int sumCosts(ArrayList<Integer> costs) {
        int total = 0;
        for (int cost : costs) {
            total += cost;
        }
        return total;
    }

    public static void WriteCSV() {
            int min_spend = sumCosts(option1cost);
            int max_spend = sumCosts(option2cost);
            int spend = totalSpent;
            File fileName = new File("C:\\Users\\GlenF\\IdeaProjects\\AdaHack24\\Lib\\output.csv");
            try (FileWriter csvWriter = new FileWriter(fileName)) {
                csvWriter.append(String.valueOf(spend))
                        .append("\n")
                        .append(String.valueOf(min_spend))
                        .append("\n")
                        .append(String.valueOf(max_spend))
                        .append("\n");

                System.out.println("Data written to output.csv");
            } catch (IOException e) {
                e.printStackTrace();

        }
    }

        public static void executePy() {
            try {
                // Define the command to execute the Python script
                ProcessBuilder pb = new ProcessBuilder("python", "C:\\Users\\GlenF\\IdeaProjects\\AdaHack24\\src\\main.py");

                // Redirect error and output streams
                pb.redirectErrorStream(true);

                // Start the process
                Process process = pb.start();

                // Capture output from the Python script
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
                // Wait for the process to finish
                int exitCode = process.waitFor();
                System.out.println("Python script finished with exit code: " + exitCode);

            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }
        }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Daily Financial");
        frame.setContentPane(new DailyFinancial().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
    }
}
