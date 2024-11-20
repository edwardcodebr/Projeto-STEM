package fisica;
import javax.swing.JOptionPane;

public class Calcfisic {

    public static void calcularEnergiaCinetica() {
        double massa = Double.parseDouble(JOptionPane.showInputDialog("Digite a massa (kg):"));
        double velocidade = Double.parseDouble(JOptionPane.showInputDialog("Digite a velocidade (m/s):"));
        double energiaCinetica = 0.5 * massa * Math.pow(velocidade, 2);
        JOptionPane.showMessageDialog(null, "Energia Cinética: " + energiaCinetica + " Joules");
    }

    public static void calcularForcaAtrito() {
        double coefAtrito = Double.parseDouble(JOptionPane.showInputDialog("Digite o coeficiente de atrito:"));
        double normal = Double.parseDouble(JOptionPane.showInputDialog("Digite a força normal (N):"));
        double forcaAtrito = coefAtrito * normal;
        JOptionPane.showMessageDialog(null, "Força de Atrito: " + forcaAtrito + " N");
    }

    public static void calcularForca() {
        double massa = Double.parseDouble(JOptionPane.showInputDialog("Digite a massa (kg):"));
        double aceleracao = Double.parseDouble(JOptionPane.showInputDialog("Digite a aceleração (m/s²):"));
        double forca = massa * aceleracao;
        JOptionPane.showMessageDialog(null, "Força: " + forca + " N");
    }

    public static void calcularVelocidadeOnda() {
        double frequencia = Double.parseDouble(JOptionPane.showInputDialog("Digite a frequência (Hz):"));
        double comprimento = Double.parseDouble(JOptionPane.showInputDialog("Digite o comprimento de onda (m):"));
        double velocidade = frequencia * comprimento;
        JOptionPane.showMessageDialog(null, "Velocidade da Onda: " + velocidade + " m/s");
    }

    public static void calcularOndaSenoidal() {
        JOptionPane.showMessageDialog(null, "Uma onda senoidal pode ser representada pela equação: y(x, t) = A * sin(kx - ωt + φ)");
    }

    public static void calcularOndaEletromagnetica() {
        JOptionPane.showMessageDialog(null, "A velocidade de uma onda eletromagnética no vácuo é aproximadamente 299.792.458 m/s (velocidade da luz).");
    }

    public static void mostrarForcaGravitacional() {
        double massa1 = Double.parseDouble(JOptionPane.showInputDialog("Digite a massa do primeiro objeto (kg):"));
        double massa2 = Double.parseDouble(JOptionPane.showInputDialog("Digite a massa do segundo objeto (kg):"));
        double distancia = Double.parseDouble(JOptionPane.showInputDialog("Digite a distância entre os objetos (m):"));
        double G = 6.67430e-11; // Constante gravitacional
        double forca = G * massa1 * massa2 / Math.pow(distancia, 2);
        JOptionPane.showMessageDialog(null, "Força Gravitacional: " + forca + " N");
    }

    public static void equacaoBernoulli() {
        JOptionPane.showMessageDialog(null, "A equação de Bernoulli é: P + 0.5ρv² + ρgh = constante.");
    }

    public static void medirEletricidade() {
        double tensao = Double.parseDouble(JOptionPane.showInputDialog("Digite a tensão (V):"));
        double corrente = Double.parseDouble(JOptionPane.showInputDialog("Digite a corrente (A):"));
        double resistencia = tensao / corrente;
        JOptionPane.showMessageDialog(null, "Resistência: " + resistencia + " ohms");
    }

    public static void medirCapacitancia() {
        double carga = Double.parseDouble(JOptionPane.showInputDialog("Digite a carga (C):"));
        double tensao = Double.parseDouble(JOptionPane.showInputDialog("Digite a tensão (V):"));
        double capacitancia = carga / tensao;
        JOptionPane.showMessageDialog(null, "Capacitância: " + capacitancia + " F");
    }

    public static void calcularLancamentoObliquo() {
        double velocidadeInicial = Double.parseDouble(JOptionPane.showInputDialog("Digite a velocidade inicial (m/s):"));
        double angulo = Double.parseDouble(JOptionPane.showInputDialog("Digite o ângulo de lançamento (graus):"));
        double alturaInicial = Double.parseDouble(JOptionPane.showInputDialog("Digite a altura inicial (m):"));
        double gravidade = 9.8; // Gravidade padrão da Terra

        double anguloRad = Math.toRadians(angulo);
        double alcance = (velocidadeInicial * Math.cos(anguloRad) / gravidade) *
                         (velocidadeInicial * Math.sin(anguloRad) + 
                         Math.sqrt(Math.pow(velocidadeInicial * Math.sin(anguloRad), 2) + 2 * gravidade * alturaInicial));
        double alturaMax = alturaInicial + Math.pow(velocidadeInicial * Math.sin(anguloRad), 2) / (2 * gravidade);

        JOptionPane.showMessageDialog(null, "Alcance: " + alcance + " m\nAltura Máxima: " + alturaMax + " m");
    }

    public static void main(String[] args) {
        String[] opcoes = {
                "Energia Cinética", "Força de Atrito", "Força", "Velocidade de Onda", 
                "Onda Senoidal", "Onda Eletromagnética", "Força Gravitacional",
                "Equação de Bernoulli", "Eletricidade", "Capacitância", 
                "Lançamento Oblíquo", "Sair"
        };

        while (true) {
            int escolha = JOptionPane.showOptionDialog(null, "Escolha um cálculo ou explicação", "Calculadora Física",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, opcoes, opcoes[0]);

            if (escolha == -1 || "Sair".equals(opcoes[escolha])) {
                JOptionPane.showMessageDialog(null, "Encerrando a aplicação.");
                break;
            }

            switch (escolha) {
                case 0 -> calcularEnergiaCinetica();
                case 1 -> calcularForcaAtrito();
                case 2 -> calcularForca();
                case 3 -> calcularVelocidadeOnda();
                case 4 -> calcularOndaSenoidal();
                case 5 -> calcularOndaEletromagnetica();
                case 6 -> mostrarForcaGravitacional();
                case 7 -> equacaoBernoulli();
                case 8 -> medirEletricidade();
                case 9 -> medirCapacitancia();
                case 10 -> calcularLancamentoObliquo();
                default -> JOptionPane.showMessageDialog(null, "Opção inválida!");
            }
        }
    }
}
